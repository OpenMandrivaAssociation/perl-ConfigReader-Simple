
%define realname   ConfigReader-Simple
%define version    1.27
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Read simple configuration file formats
Source:     http://www.cpan.org/modules/by-module/ConfigReader/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Test::Warn)

BuildArch: noarch

%description
'ConfigReader::Simple' reads and parses simple configuration files. It is
designed to be smaller and simpler than the 'ConfigReader' module and is
more suited to simple configuration files. 

The configuration file format
    The configuration file uses a line-oriented format, meaning that the
    directives do not have containers. The values can be split across lines
    with a continuation character, but for the most part everything ends up
    on the same line.

    The first group of non-whitespace characters is the "directive", or the
    name of the configuration item. The linear whitespace after that
    separates the directive from the "value", which is the rest of the
    line, including any other whitespace.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


