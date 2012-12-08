%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 2.1.5-1
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Catalan
%define languagecode ca
%define lc_ctype ca_ES

Summary:       %{languageenglazy} files for aspell
Summary(ca):   Diccionari català per aspell
Name:          aspell-%{languagecode}
Version:       20090721
Release:       %mkrel 4
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:           http://aspell.net/
License:	GPLv2
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-ca


BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%description -l ca
aspell-ca té les dades d'ortografia del català per utilitzar-se amb
el programa ispell. Amb aquesta extensió, podeu redactar un document
en català i verificar fàcilment les seves errades.

aspell es pot utilitzar directament des de la línia d'ordres
per tal de verificar un fitxer o utilitzat per diversos programes
comercials de text, com el Lyx, etc."

%prep
%setup -q -n %{fname}-%{src_ver}
iconv -f ISO-8859-15 -t utf-8 doc/ChangeLog -o doc/ChangeLog.aux
iconv -f ISO-8859-15 -t utf-8 Copyright -o Copyright.aux
mv -f doc/ChangeLog.aux doc/ChangeLog
mv -f Copyright.aux Copyright

%build

# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

mv -f README README.%{languagecode}
chmod 644 Copyright README.%{languagecode} doc/*

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.%{languagecode} Copyright doc/*
%{_libdir}/aspell-%{aspell_ver}/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 20090721-3mdv2011.0
+ Revision: 662801
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 20090721-2mdv2011.0
+ Revision: 603196
- rebuild

* Sun Mar 14 2010 Isabel Vallejo <isabel@mandriva.org> 20090721-1mdv2010.1
+ Revision: 519095
- update to 2009-07-21.1
- update to 2.1.5-9
- update to 2.1.5
- update to 2.1.5

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 20040130.1-8mdv2010.1
+ Revision: 518910
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 20040130.1-7mdv2010.0
+ Revision: 413051
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 20040130.1-6mdv2009.1
+ Revision: 350002
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 20040130.1-5mdv2009.0
+ Revision: 220365
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 20040130.1-4mdv2008.1
+ Revision: 182405
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 20040130.1-3mdv2008.1
+ Revision: 148742
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 20040130.1-2mdv2007.0
+ Revision: 123229
- Import aspell-ca

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 20040130.1-2mdv2007.1
- use the mkrel macro
- disable debug packages

* Fri Dec 03 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 20040130.1-1mdk
- new release

* Wed Jul 28 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.50.2-5mdk
- allow build on ia64

