%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 2.1.5-1
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Catalan
%define languagecode ca
%define lc_ctype ca_ES

Summary:	%{languageenglazy} files for aspell
Summary(ca):	Diccionari català per aspell
Name:		aspell-%{languagecode}
Version:	20090721
Release:	12
Group:		System/Internationalization
License:	GPLv2
Url:		http://aspell.net/
Source0:	http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= %{aspell_ver}
Requires:	aspell >= %{aspell_ver}
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}
Provides:	spell-ca
Autoreqprov:	no

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
%setup -qn %{fname}-%{src_ver}
iconv -f ISO-8859-15 -t utf-8 doc/ChangeLog -o doc/ChangeLog.aux
iconv -f ISO-8859-15 -t utf-8 Copyright -o Copyright.aux
mv -f doc/ChangeLog.aux doc/ChangeLog
mv -f Copyright.aux Copyright

%build
# don't use configure macro
./configure

%make

%install
%makeinstall_std

mv -f README README.%{languagecode}
chmod 644 Copyright README.%{languagecode} doc/*

%files
%doc README.%{languagecode} Copyright doc/*
%{_libdir}/aspell-%{aspell_ver}/*

