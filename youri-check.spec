%define name	youri-check
%define version 0.10
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Youri check tool
License:	GPL or Artistic
Group:		Development/Other
Source:		http://youri.zarb.or/download/%{name}-%{version}.tar.bz2
Url:		http://youri.zarb.org
BuildRequires:	perl(Youri::Utils)
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

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc ChangeLog README
%config(noreplace) %{_sysconfdir}/youri
%{_bindir}/youri-check
%{_mandir}/man1/*
%{_datadir}/youri
%{_sysconfdir}/bash_completion.d/%{name}
