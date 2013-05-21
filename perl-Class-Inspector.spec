%define upstream_name	 Class-Inspector
%define upstream_version 1.28

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Get information about a class and its structure 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

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
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/*/*



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.250.0-4mdv2012.0
+ Revision: 765087
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.250.0-3
+ Revision: 763531
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.250.0-2
+ Revision: 667044
- mass rebuild

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.250.0-1
+ Revision: 634212
- update to new version 1.25

* Thu Jul 16 2009 Jérôme Quelin <jquelin@mandriva.org> 1.240.0-1mdv2010.1
+ Revision: 396562
- rebuild to make perl-Test-ClassAPI happy
- using %%perl_convert_version
- fixed license field

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.24-1mdv2010.0
+ Revision: 370041
- update to new version 1.24

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.23-2mdv2009.0
+ Revision: 268399
- rebuild early 2009.0 package (before pixel changes)

* Tue Jun 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.23-1mdv2009.0
+ Revision: 214510
- update to new version 1.23

* Mon Mar 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.22-1mdv2008.1
+ Revision: 177894
- update to new version 1.22

* Tue Feb 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-1mdv2008.1
+ Revision: 166568
- new version
- re-add buildroot titi kindly removed before making it a submission rejection reason...

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.18-1mdv2008.1
+ Revision: 109509
- update to new version 1.18

* Wed Aug 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.17-1mdv2008.0
+ Revision: 63924
- update to new version 1.17


* Mon Aug 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.16-2mdv2007.0
- Rebuild

* Thu May 11 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.16-1mdk
- New release 1.16

* Tue May 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.15-1mdk
- New release 1.15

* Mon Apr 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.14-1mdk
- New release 1.14
- better source URL

* Wed Apr 05 2006 Buchan Milne <bgmilne@mandriva.org> 1.13-2mdk
- use mkrel

* Fri Sep 30 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.13-1mdk
- New release 1.13
- spec cleanup

* Wed Sep 21 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-1mdk
- New release 1.12

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.08-1mdk
- initial Mandriva package

