%define upstream_name	 Class-Inspector
%define upstream_version 1.25

Name:		    perl-%{upstream_name}
Version:	    %perl_convert_version %{upstream_version}
Release:	    %mkrel 4

Summary:	    Get information about a class and its structure 
License:	    GPL+ or Artistic
Group:		    Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Class::Inspector allows you to get information about a loaded class.
Most or all of this information can be found in other ways, but they
arn't always very friendly, and usually involve a relatively high level
of Perl wizardry, or strange and unusual looking code. Class::Inspector
attempts to provide an easier, more friendly interface to this
information.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/*/*

