#!/bin/sh
##### -*- mode:shell-script; indent-tabs-mode:nil; sh-basic-offset:2 -*-

src_repo="$(pwd)"

if [ ! -d .git ]; then
  echo "error: must be run from within the top level of a FluxPBX git tree." 1>&2
  exit 1;
fi

ver="1.0.50"

basedir=$(pwd);

(mkdir -p rpmbuild && cd rpmbuild && mkdir -p SOURCES BUILD BUILDROOT i386 x86_64 SPECS)

if [ ! -d "$basedir/../fluxpbx-sounds" ]; then
        cd $basedir/..
        git clone https://fluxpbx.org/stash/scm/fs/fluxpbx-sounds.git
else
        cd $basedir/../fluxpbx-sounds
        git pull
fi

cd $basedir/../fluxpbx-sounds/sounds/trunk
./dist.pl music
mv fluxpbx-sounds-music-*.tar.gz $basedir/rpmbuild/SOURCES

cd $basedir

rpmbuild --define "VERSION_NUMBER $ver" \
  --define "BUILD_NUMBER 1" \
  --define "_topdir %(pwd)/rpmbuild" \
  --define "_rpmdir %{_topdir}" \
  --define "_srcrpmdir %{_topdir}" \
  -ba fluxpbx-sounds-music.spec

mkdir $src_repo/RPMS
mv $src_repo/rpmbuild/*/*.rpm $src_repo/RPMS/.

cat 1>&2 <<EOF
----------------------------------------------------------------------
The Sound RPMs have been rolled
----------------------------------------------------------------------
EOF

