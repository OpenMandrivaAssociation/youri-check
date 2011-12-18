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
Url:		http://youri.zarb.org
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
