# template spec file
# Refer to the following for more info on .spec file syntax:
#   http://www.rpm.org/max-rpm/
#   http://www.rpm.org/max-rpm-snapshot/	(Updated version of above)
#   http://docs.fedoraproject.org/drafts/rpm-guide-en/
# More links may be available from http://www.rpm.org

# A collection of magic to set the release "number" such that dist upgrades will, erm, upgrade.
# NB:  This really only applies to packages built with debbuild.
%if %{?debdist:0}%{?!debdist:1}
%define debdist etch
%endif
%if "%{debdist}" == "sarge"
%define errata 0
%endif
%if "%{debdist}" == "dapper"
%define errata 1
%endif
%if "%{debdist}" == "etch"
%define errata 2
%endif
%if "%{debdist}" == "lenny"
%define errata 3
%endif
%if %{?relnum:0}%{?!relnum:1}
%define relnum 1
%endif

# %{_vendor} is only set to "redhat" on Red Hat (Enterprise) Linux and direct
# derivatives/ancestors (eg Fedora Core).  Upstream rpm (as packaged in Debian,
# for instance) sets it to "rpm".  debbuild sets it to "debbuild".
%if %{_vendor} == "redhat"
%define errata el4
%define release %{relnum}.%{errata}
%else
%define release %{relnum}.%{errata}%{debdist}
%endif

Summary: one-line description
Name: package
Version: 0.0.0.1
Release: %{release}
Source: http://site/tarball
Group: Applications/System
License: GPL
Packager: Name <email@site>
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Multi-line
description

%prep
# Steps to unpack and patch source as needed
%setup -q

%build
# Steps to compile the source
%configure
make

%install
# Steps to install to a temporary location for packaging
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%makeinstall

# Fill in the pathnames to be packaged here
%files
%{_bindir}/*
%{_mandir}/man1/*
%doc README

%changelog
* Mon Jan 01 1900  Name <email@site> -relnum
- Packaging comment
