######################################################################################################################
#
# fluxpbx-config-rayo for FluxPBX Modular Media Switching Software Library / Soft-Switch Application
# Copyright (C) 2013-2015, Grasshopper
#
# Version: MPL 1.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is fluxpbx-config-rayo for FluxPBX Modular Media Switching Software Library / Soft-Switch Application
#
# The Initial Developer of the Original Code is Grasshopper
# Portions created by the Initial Developer are Copyright (C)
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
# Chris Rienzo <crienzo@grasshopper.com>
#
# fluxpbx-rayo-config -- RPM packaging for Rayo Server configuration
#
######################################################################################################################

%define nonparsedversion 1.7.0
%define version %(echo '%{nonparsedversion}' | sed 's/-//g')
%define release 1

%define fsname fluxpbx

%define	PREFIX		%{_prefix}
%define EXECPREFIX	%{_exec_prefix}
%define BINDIR		%{_bindir}
%define SBINDIR		%{_sbindir}
%define LIBEXECDIR	%{_libexecdir}/%fsname
%define SYSCONFDIR	%{_sysconfdir}/%fsname
%define SHARESTATEDIR	%{_sharedstatedir}/%fsname
%define LOCALSTATEDIR	%{_localstatedir}/lib/%fsname
%define LIBDIR		%{_libdir}
%define INCLUDEDIR	%{_includedir}
%define _datarootdir	%{_prefix}/share
%define DATAROOTDIR	%{_datarootdir}
%define DATADIR		%{_datadir}
%define INFODIR		%{_infodir}
%define LOCALEDIR	%{_datarootdir}/locale
%define MANDIR		%{_mandir}
%define DOCDIR		%{_defaultdocdir}/%fsname
%define HTMLDIR		%{_defaultdocdir}/%fsname/html
%define DVIDIR		%{_defaultdocdir}/%fsname/dvi
%define PDFDIR		%{_defaultdocdir}/%fsname/pdf
%define PSDIR		%{_defaultdocdir}/%fsname/ps
%define LOGFILEDIR	/var/log/%fsname
%define MODINSTDIR	%{_libdir}/%fsname/mod
%define RUNDIR		%{_localstatedir}/run/%fsname
%define DBDIR		%{LOCALSTATEDIR}/db
%define HTDOCSDIR	%{_datarootdir}/%fsname/htdocs
%define SOUNDSDIR	%{_datarootdir}/%fsname/sounds
%define GRAMMARDIR	%{_datarootdir}/%fsname/grammar
%define SCRIPTDIR	%{_datarootdir}/%fsname/scripts
%define RECORDINGSDIR	%{LOCALSTATEDIR}/recordings
%define PKGCONFIGDIR	%{_datarootdir}/%fsname/pkgconfig
%define HOMEDIR		%{LOCALSTATEDIR}

Name: fluxpbx-config-rayo
Version: %{version}
Release: %{release}%{?dist}
License: MPL1.1
Summary: Rayo configuration for the FluxPBX Open Source telephone platform.
Group: System/Libraries
Packager: Chris Rienzo
URL: http://www.freeswitch.org/
Source0: fluxpbx-%{nonparsedversion}.tar.bz2
Requires: fluxpbx
Requires: fluxpbx-application-conference
Requires: fluxpbx-application-esf
Requires: fluxpbx-application-expr
Requires: fluxpbx-application-fsv
Requires: fluxpbx-application-http-cache
Requires: fluxpbx-asrtts-flite
Requires: fluxpbx-asrtts-pocketsphinx
Requires: fluxpbx-codec-h26x
Requires: fluxpbx-codec-ilbc
Requires: fluxpbx-codec-opus
Requires: fluxpbx-codec-vp8
Requires: fluxpbx-event-rayo
Requires: fluxpbx-format-local-stream
Requires: fluxpbx-format-mod-shout
Requires: fluxpbx-format-shell-stream
Requires: fluxpbx-format-ssml
Requires: fluxpbx-sounds-music-8000
Requires: fluxpbx-lang-en
Requires: fluxpbx-sounds-pt-BR-karina-8000
BuildRequires: bash
BuildArch: noarch
BuildRoot:    %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
FluxPBX rayo server implementation.

%prep
%setup -b0 -q -n fluxpbx-%{nonparsedversion}

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m 0750 %{buildroot}/%{SYSCONFDIR}
%{__install} -d -m 0750 %{buildroot}/%{SYSCONFDIR}/autoload_configs
%{__install} -d -m 0750 %{buildroot}/%{SYSCONFDIR}/dialplan
%{__install} -d -m 0750 %{buildroot}/%{SYSCONFDIR}/sip_profiles
%{__install} -d -m 0750 %{buildroot}/%{SYSCONFDIR}/directory
%{__cp} -prv ./conf/rayo/*.{xml,types,pem} %{buildroot}/%{SYSCONFDIR}/
%{__cp} -prv ./conf/rayo/{autoload_configs,dialplan} %{buildroot}/%{SYSCONFDIR}/
%{__cp} -prv ./conf/rayo/sip_profiles/external.xml %{buildroot}/%{SYSCONFDIR}/sip_profiles
%{__cp} -prv ./conf/rayo/sip_profiles/external %{buildroot}/%{SYSCONFDIR}/sip_profiles
%{__cp} -prv ./conf/rayo/directory %{buildroot}/%{SYSCONFDIR}/

%postun

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,fluxpbx,daemon)
%dir %attr(0750, fluxpbx, daemon) %{SYSCONFDIR}
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/cacert.pem
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/*.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/mime.types
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/autoload_configs/acl.conf.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/autoload_configs/cdr_csv.conf.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/autoload_configs/conference.conf.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/autoload_configs/console.conf.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/autoload_configs/event_socket.conf.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/autoload_configs/http_cache.conf.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/autoload_configs/local_stream.conf.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/autoload_configs/logfile.conf.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/autoload_configs/modules.conf.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/autoload_configs/pocketsphinx.conf.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/autoload_configs/post_load_modules.conf.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/autoload_configs/presence_map.conf.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/autoload_configs/rayo.conf.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/autoload_configs/shout.conf.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/autoload_configs/sofia.conf.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/autoload_configs/spandsp.conf.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/autoload_configs/ssml.conf.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/autoload_configs/switch.conf.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/autoload_configs/timezones.conf.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/dialplan/public.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/directory/default.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/directory/default/*.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/sip_profiles/*.xml
%config(noreplace) %attr(0640, fluxpbx, daemon) %{SYSCONFDIR}/sip_profiles/external/*.xml

### END OF config-rayo

######################################################################################################################
#
#						Changelog
#
######################################################################################################################
%changelog
* Tue Apr 23 2019 - Andrey Volk
- Fix build for Stack 20.x
* Tue Jun 10 2014 crienzo@grasshopper.com
- Remove dependency to high resolution music and sounds files
- Remove dependency to specific FluxPBX package version
* Mon Jun 03 2013 - crienzo@grasshopper.com
- Added users and internal profile for softphone testing
* Wed May 08 2013 - crienzo@grasshopper.com
- Initial revision

