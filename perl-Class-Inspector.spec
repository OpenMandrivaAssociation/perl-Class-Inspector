%define upstream_name	 Class-Inspector
%define upstream_version 1.28

Summary:	Get information about a class and its structure 
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Class::Inspector allows you to get information about a loaded class.
Most or all of this information can be found in other ways, but they
arn't always very friendly, and usually involve a relatively high level
of Perl wizardry, or strange and unusual looking code. Class::Inspector
attempts to provide an easier, more friendly interface to this
information.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/man3/*

