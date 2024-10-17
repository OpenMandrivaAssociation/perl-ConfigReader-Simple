%define upstream_name    ConfigReader-Simple
%define upstream_version 1.28

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Read simple configuration file formats
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/ConfigReader/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Output)
BuildRequires:	perl(Test::Warn)
BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.280.0-3mdv2011.0
+ Revision: 658743
- rebuild for updated spec-helper

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.280.0-2mdv2011.0
+ Revision: 551997
- rebuild

* Wed Jun 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.280.0-1mdv2010.0
+ Revision: 386764
- adding missing buildrequires:
- update to 1.28
- using %%perl_convert_version
- fix license

* Sat Sep 06 2008 Jérôme Quelin <jquelin@mandriva.org> 1.27-1mdv2009.0
+ Revision: 281793
- import perl-ConfigReader-Simple


* Sat Sep 06 2008 cpan2dist 1.27-1mdv
- initial mdv release, generated with cpan2dist

