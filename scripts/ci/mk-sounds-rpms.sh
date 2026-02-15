#!/bin/sh
##### -*- mode:shell-script; indent-tabs-mode:nil; sh-basic-offset:2 -*-

declare -a specfiles=('fluxpbx-sounds-en-ca-june.spec' 'fluxpbx-sounds-en-us-allison.spec' 'fluxpbx-sounds-fr-ca-june.spec' 'fluxpbx-sounds-music.spec' 'fluxpbx-sounds-pt-BR-karina.spec' 'fluxpbx-sounds-ru-RU-elena.spec' 'fluxpbx-sounds-pt-BR-karina.spec' 'fluxpbx-sounds-sv-se-jakob.spec')

sdir="."
[ -n "${0%/*}" ] && sdir="${0%/*}"
. $sdir/common.sh

check_pwd

basedir=$(pwd);

(mkdir -p rpmbuild && cd rpmbuild && mkdir -p SOURCES BUILD BUILDROOT i386 x86_64 SPECS)

if [ ! -d "$basedir/../fluxpbx-sounds" ]; then
	cd $basedir/..
	git clone https://fluxpbx.org/stash/scm/fs/fluxpbx-sounds.git
else
	cd $basedir/../fluxpbx-sounds
	git clean -fdx
	git pull
fi

for i in "${specfiles[@]}"
do

cd $basedir/../fluxpbx-sounds/

./dist.pl `echo $i|sed -e 's/fluxpbx-sounds-//g' -e 's/\.spec//g' -e 's/-/\//g'`

mv `echo $i|sed -e's/\.spec//g'`*.tar.* $basedir/rpmbuild/SOURCES

cd $basedir

rpmbuild --define "_topdir %(pwd)/rpmbuild" \
  --define "_rpmdir %{_topdir}" \
  --define "_srcrpmdir %{_topdir}" \
  -ba $i

done

mkdir $src_repo/RPMS
mv $src_repo/rpmbuild/*/*.rpm $src_repo/RPMS/.

cat 1>&2 <<EOF
----------------------------------------------------------------------
The Sound RPMs have been rolled
----------------------------------------------------------------------
EOF
