%define name	youri-check
%define version 0.10.1
%define release %mkrel 2

%define _provides_exceptions perl(Youri::Check::.*)
%define _requires_exceptions perl(Youri::\\(Check::.*\\|BTS::Bugzilla\\))

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Youri check tool
License:	GPL or Artistic
Group:		Development/Other
Source:		http://youri.zarb.or/download/%{name}-%{version}.tar.bz2
Url:		https://youri.zarb.org
BuildRequires:	perl-Youri-Utils
# avoid mandriva fork
Requires:	    perl-Youri-Config
Requires:	    perl-Youri-Package
Requires:	    perl-Youri-Utils
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
youri-check is a generic package checking tools. It runs a list of tests on a
list of package sets, and produces corresponding reports.

%prep
%setup -q

%build
%configure2_5x
%make

%check
%__make check

%install
rm -rf %{buildroot}
%makeinstall_std
cat > README.urpmi<<EOF
Mandriva RPM specific notes

post-installation
-----------------
You need to setup a database, and install related DBI drivers. There is no
schema to create, the application will do it automatically.

You also need to adapt the configuration file to suite your needs, the one
provided is only intended as an example. More details on YAML syntax can be
found in YAML::AppConfig man page.
EOF

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc ChangeLog README README.urpmi
%config(noreplace) %{_sysconfdir}/youri
%{_bindir}/youri-check
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_datadir}/youri
%{_sysconfdir}/bash_completion.d/%{name}


%changelog
* Sun Dec 18 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10.1-2mdv2012.0
+ Revision: 743476
- bump release
- 0.10.1

* Wed Jul 21 2010 Thierry Vignaud <tv@mandriva.org> 0.10-6mdv2011.0
+ Revision: 556500
- rebuild for new perl

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 0.10-5mdv2010.0
+ Revision: 446311
- rebuild

* Sun Jan 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-4mdv2009.1
+ Revision: 324644
- use explicit dependencies, to avoid mandriva fork package
- filter some useless automatic dependencies
- add README.urpmi with a few post-installation details

* Tue Aug 05 2008 Thierry Vignaud <tv@mandriva.org> 0.10-3mdv2009.0
+ Revision: 263762
- fix testsuite buildrequires
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Apr 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2008.0
+ Revision: 17081
- Import youri-check



* Sun Apr 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2008.0
- first mdv release
