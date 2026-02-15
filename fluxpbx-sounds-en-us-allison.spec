##############################################################################
# Copyright and license
##############################################################################
#
# Spec file for package fluxpbx-sounds-en-us-allison (version 1.0.1-1)
#
# Copyright (c) 2009 Patrick Laimbock 
# Some fixes and additions (c) 2011 Michal Bielicki
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

##############################################################################
# Determine distribution
##############################################################################

# %define is_rhel5 %(test -f /etc/redhat-release && egrep -q 'release 5' /etc/redhat-release && echo 1 || echo 0)

##############################################################################
# Set variables
##############################################################################

%define version 1.0.1
%define release 1

%define fsname  fluxpbx
# you could add a version number to be more strict

%define PREFIX          %{_prefix}
%define EXECPREFIX      %{_exec_prefix}
%define BINDIR          %{_bindir}
%define SBINDIR         %{_sbindir}
%define LIBEXECDIR      %{_libexecdir}/%{fsname}
%define SYSCONFDIR      %{_sysconfdir}/%{fsname}
%define SHARESTATEDIR   %{_sharedstatedir}/%{fsname}
%define LOCALSTATEDIR   %{_localstatedir}/lib/%{fsname}
%define LIBDIR          %{_libdir}
%define INCLUDEDIR      %{_includedir}
%define _datarootdir    %{_prefix}/share
%define DATAROOTDIR     %{_datarootdir}
%define DATADIR         %{_datadir}
%define INFODIR         %{_infodir}
%define LOCALEDIR       %{_datarootdir}/locale
%define MANDIR          %{_mandir}
%define DOCDIR          %{_defaultdocdir}/%{fsname}
%define HTMLDIR         %{_defaultdocdir}/%{fsname}/html
%define DVIDIR          %{_defaultdocdir}/%{fsname}/dvi
%define PDFDIR          %{_defaultdocdir}/%{fsname}/pdf
%define PSDIR           %{_defaultdocdir}/%{fsname}/ps
%define LOGFILEDIR      /var/log/%{fsname}
%define MODINSTDIR      %{_libdir}/%{fsname}/mod
%define RUNDIR          %{_localstatedir}/run/%{fsname}
%define DBDIR           %{LOCALSTATEDIR}/db
%define HTDOCSDIR       %{_datarootdir}/%{fsname}/htdocs
%define SOUNDSDIR       %{_datarootdir}/%{fsname}/sounds
%define GRAMMARDIR      %{_datarootdir}/%{fsname}/grammar
%define SCRIPTDIR       %{_datarootdir}/%{fsname}/scripts
%define RECORDINGSDIR   %{LOCALSTATEDIR}/recordings
%define PKGCONFIGDIR    %{_datarootdir}/%{fsname}/pkgconfig
%define HOMEDIR         %{LOCALSTATEDIR}


##############################################################################
# General
##############################################################################

Summary: FluxPBX en-us Allison prompts
Name: fluxpbx-sounds-en-us-allison
Version: %{version}
Release: %{release}%{?dist}
License: MPL
Group: Applications/Communications
Packager: Patrick Laimbock <vc-rpms@voipconsulting.nl>
URL: http://www.freeswitch.org
Source0:https://sbcdev4.flux.net.br/freeswitch/sounds/%{name}-48000-%{version}.tar.gz
Source1:https://sbcdev4.flux.net.br/freeswitch/sounds/%{name}-32000-%{version}.tar.gz
Source2:https://sbcdev4.flux.net.br/freeswitch/sounds/%{name}-16000-%{version}.tar.gz
Source3:https://sbcdev4.flux.net.br/freeswitch/sounds/%{name}-8000-%{version}.tar.gz
BuildArch: noarch
BuildRequires: sox
Requires: fluxpbx
Requires: fluxpbx-sounds-en-us-allison-48000
Requires: sox
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
FluxPBX 48kHz en-us Allison prompts plus, during the installation,
it will also install locally generated 8KHz, 16KHz and 32KHz prompts

%package -n fluxpbx-sounds-en-us-allison-8000
Summary: FluxPBX 8kHz en-us Allison prompts
Group: Applications/Communications
BuildArch: noarch
Requires: %{fsname}

%description -n fluxpbx-sounds-en-us-allison-8000
FluxPBX 8kHz en-us Allison prompts

%package -n fluxpbx-sounds-en-us-allison-16000
Summary: FluxPBX 16kHz en-us Allison prompts
Group: Applications/Communications
BuildArch: noarch
Requires: %{fsname}

%description -n fluxpbx-sounds-en-us-allison-16000
FluxPBX 16kHz en-us Allison prompts

%package -n fluxpbx-sounds-en-us-allison-32000
Summary: FluxPBX 32kHz en-us Allison prompts
Group: Applications/Communications
BuildArch: noarch
Requires: %{fsname}

%description -n fluxpbx-sounds-en-us-allison-32000
FluxPBX 32kHz en-us Allison prompts

%package -n fluxpbx-sounds-en-us-allison-48000
Summary: FluxPBX 48kHz en-us Allison prompts
Group: Applications/Communications
BuildArch: noarch
Requires: %{fsname}

%description -n fluxpbx-sounds-en-us-allison-48000
FluxPBX 48kHz en-us Allison prompts

%package -n fluxpbx-sounds-en-us-allison-all
Summary: FluxPBX en-us Allison prompts
Group: Applications/Communications
BuildArch: noarch
Requires: %{fsname}
Requires: fluxpbx-sounds-en-us-allison-8000 = %{version}
Requires: fluxpbx-sounds-en-us-allison-16000 = %{version}
Requires: fluxpbx-sounds-en-us-allison-32000 = %{version}
Requires: fluxpbx-sounds-en-us-allison-48000 = %{version}

%description -n fluxpbx-sounds-en-us-allison-all
FluxPBX Allison prompts package that pulls in the 8KHz, 16KHz,
32KHz and 48KHz RPMs

##############################################################################
# Prep
##############################################################################

%prep
%setup -n en
%setup -T -D -b 0 -n en
%setup -T -D -b 1 -n en
%setup -T -D -b 2 -n en
%setup -T -D -b 3 -n en

##############################################################################
# Build
##############################################################################

%build
# nothing to do here

##############################################################################
# Install
##############################################################################

%install
[ "%{buildroot}" != '/' ] && rm -rf %{buildroot}

# create the sounds directories
%{__install} -d -m 0750 %{buildroot}%{SOUNDSDIR}/en/us/allison

pushd us/allison
# first install the 48KHz sounds
%{__cp} -prv ./* %{buildroot}%{SOUNDSDIR}/en/us/allison
# now resample the 48KHz ones to 8KHz, 16KHz and 32KHz
popd

##############################################################################
# Clean
##############################################################################

%clean
[ "%{buildroot}" != '/' ] && rm -rf %{buildroot}

##############################################################################
# Post
##############################################################################

%post
# generate the 8KHz, 16KHz and 32KHz prompts from the 48KHz ones

##############################################################################
# Postun
##############################################################################

%postun
# you could check if there are sound files in 8000/ or
# 16000/ or 32000/ and remove them *only* if the files
# do not belong to an rpm

##############################################################################
# Files
##############################################################################

%files
%defattr(-,root,root)

%files -n fluxpbx-sounds-en-us-allison-8000
%defattr(-,root,root,-)
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/alt/8000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/ascii/8000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/base256/8000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/conference/8000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/currency/8000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/digits/8000
%attr(0750,fluxpbx,daemon)   %dir    %{SOUNDSDIR}/en/us/allison/directory/8000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/ivr/8000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/misc/8000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/time/8000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/voicemail/8000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/zrtp/8000
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/alt/8000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/ascii/8000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/base256/8000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/conference/8000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/currency/8000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/digits/8000/*.wav
%attr(0640,fluxpbx,daemon)           %{SOUNDSDIR}/en/us/allison/directory/8000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/ivr/8000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/misc/8000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/time/8000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/voicemail/8000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/zrtp/8000/*.wav

%files -n fluxpbx-sounds-en-us-allison-16000
%defattr(-,root,root,-)
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/alt/16000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/ascii/16000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/base256/16000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/conference/16000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/currency/16000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/digits/16000
%attr(0750,fluxpbx,daemon)   %dir    %{SOUNDSDIR}/en/us/allison/directory/16000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/ivr/16000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/misc/16000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/time/16000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/voicemail/16000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/zrtp/16000
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/alt/16000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/ascii/16000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/base256/16000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/conference/16000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/currency/16000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/digits/16000/*.wav
%attr(0640,fluxpbx,daemon)           %{SOUNDSDIR}/en/us/allison/directory/16000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/ivr/16000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/misc/16000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/time/16000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/voicemail/16000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/zrtp/16000/*.wav

%files -n fluxpbx-sounds-en-us-allison-32000
%defattr(-,root,root,-)
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/alt/32000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/ascii/32000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/base256/32000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/conference/32000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/currency/32000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/digits/32000
%attr(0750,fluxpbx,daemon)   %dir    %{SOUNDSDIR}/en/us/allison/directory/32000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/ivr/32000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/misc/32000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/time/32000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/voicemail/32000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/zrtp/32000
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/alt/32000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/ascii/32000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/base256/32000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/conference/32000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/currency/32000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/digits/32000/*.wav
%attr(0640,fluxpbx,daemon)           %{SOUNDSDIR}/en/us/allison/directory/32000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/ivr/32000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/misc/32000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/time/32000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/voicemail/32000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/zrtp/32000/*.wav

%files -n fluxpbx-sounds-en-us-allison-48000
%defattr(-,root,root,-)
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/alt/48000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/ascii/48000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/base256/48000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/conference/48000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/currency/48000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/digits/48000
%attr(0750,fluxpbx,daemon)   %dir    %{SOUNDSDIR}/en/us/allison/directory/48000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/ivr/48000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/misc/48000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/time/48000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/voicemail/48000
%attr(0750,fluxpbx,daemon)	%dir	%{SOUNDSDIR}/en/us/allison/zrtp/48000
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/alt/48000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/ascii/48000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/base256/48000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/conference/48000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/currency/48000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/digits/48000/*.wav
%attr(0640,fluxpbx,daemon)           %{SOUNDSDIR}/en/us/allison/directory/48000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/ivr/48000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/misc/48000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/time/48000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/voicemail/48000/*.wav
%attr(0640,fluxpbx,daemon)		%{SOUNDSDIR}/en/us/allison/zrtp/48000/*.wav

%files -n fluxpbx-sounds-en-us-allison-all

##############################################################################
# Changelog
##############################################################################

%changelog
* Fri Apr 19 2019 Andrey Volk <andrey@signalwire.com> - 1.0.1-1
- add missing alt folder and remove non-existing items
- bump up version
* Tue Jul 25 2017 Mike Jerris <mike@fluxpbx.org> - 1.0.0-1
- update to FHS Layout for FluxPBX
- bump up version

