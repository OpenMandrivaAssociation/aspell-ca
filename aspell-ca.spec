%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 20040130-1
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Catalan
%define languagecode ca
%define lc_ctype ca_ES

Summary:       %{languageenglazy} files for aspell
Summary(ca):   Diccionari català per aspell
Name:          aspell-%{languagecode}
Version:       20040130.1
Release:       %mkrel 3
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:           http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-ca


BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
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


