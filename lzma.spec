Summary:	LZMA Encoder/Decoder
Summary(pl.UTF-8):	Koder/Dekoder LZMA
Name:		lzma
Version:	4.53
Release:	1
License:	CPL/LGPL
Group:		Applications/Archiving
Source0:	http://dl.sourceforge.net/p7zip/p7zip_%{version}_src_all.tar.bz2
# Source0-md5:	331450463d5737bba96cbea2115abe8b
Patch0:		%{name}-quiet.patch
Patch1:		%{name}427_zlib.patch
Patch2:		%{name}-shared.patch
Patch3:		%{name}-lzmalib.patch
Patch4:		%{name}-makefile.patch
URL:		http://www.7-zip.org/sdk.html
BuildRequires:	libstdc++-devel
# does not need -libs, due apps being not linked with shared lib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LZMA is default and general compression method of 7z format in 7-Zip
program. LZMA provides high compression ratio and very fast
decompression, so it is very suitable for embedded applications. For
example, it can be used for ROM (firmware) compressing.

LZMA features:

- Compressing speed: 500 KB/s on 1 GHz CPU
- Decompressing speed:
  - 8-12 MB/s on 1 GHz Intel Pentium 3 or AMD Athlon.
  - 500-1000 KB/s on 100 MHz ARM, MIPS, PowerPC or other simple RISC
    CPU.
- Small memory requirements for decompressing: 8-32 KB + dictionary
  size
- Small code size for decompressing: 2-8 KB (depending from speed
  optimizations)

%description -l pl.UTF-8
LZMA jest domyślnym i ogólnym algorytmem kompresji formatu 7z
stosowanego przez 7-Zip. LZMA zapewnia wysoki stopień kompresji i
bardzo szybką dekompresję, więc nadaje się do zastosowań osadzonych.
Przykładowo, może być użyty do kompresji ROM-u (firmware'u).

Cechy LZMA:

- Szybkość kompresowania: 500 KB/s na 1 GHz procesorze,
- Szybkość dekompresowania:
  - 8-12 MB/s na 1 GHz Pentium 3 lub Athlonie,
  - 500-1000 KB/s na 100 MHz procesorach ARM, MIPS, PowerPC lub innych
    prostych RISC-ach,
- Mała ilość pamięci potrzebna do dekompresowania: 8-32 KB + rozmiar
  słownika,
- Mały rozmiar kodu dekompresującego: 2-8 KB (w zależności od opcji
  optymalizacji).

%package libs
Summary:	LZMA shared library
Summary(pl.UTF-8):	Biblioteka współdzielona LZMA
Group:		Libraries

%description libs
LZMA shared library.

%description libs -l pl.UTF-8
Biblioteka współdzielona LZMA.

%package devel
Summary:	Header file for LZMA library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki LZMA
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header file for LZMA library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki LZMA.

%package static
Summary:	LZMA static library
Summary(pl.UTF-8):	Biblioteka statyczna LZMA
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
LZMA static library.

%description static -l pl.UTF-8
Biblioteka statyczna LZMA.

%prep
%setup -q -n p7zip_%{version}
%patch0 -p1
#%patch1 -p1
#%patch2 -p1
#%patch3 -p1
%patch4 -p1

%build
cd CPP/7zip/Compress/LZMA_Alone
%{__make} -f makefile \
	CXX="%{__cxx}" \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmcflags} %{rpmldflags}"

#cd ../LZMA_Lib
#%{__make} -f makefile \
#	CXX="%{__cxx}" \
#	CFLAGS="%{rpmcflags} -c -fpic" \
#	LDFLAGS="%{rpmcflags} %{rpmldflags}"


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_libdir}}

install CPP/7zip/Compress/LZMA_Alone/lzma $RPM_BUILD_ROOT%{_bindir}
#install CPP/7zip/Compress/LZMA_Lib/lzmalib.h $RPM_BUILD_ROOT%{_includedir}
#install CPP/7zip/Compress/LZMA_Lib/liblzma.a $RPM_BUILD_ROOT%{_libdir}
#install CPP/7zip/Compress/LZMA_Lib/liblzma.so.*.*.* $RPM_BUILD_ROOT%{_libdir}
#ln -s $(cd CPP/7zip/Compress/LZMA_Lib; echo liblzma.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/liblzma.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
#%doc history.txt lzma.txt
%attr(755,root,root) %{_bindir}/*

#%files libs
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/liblzma.so.*.*

#%files devel
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/liblzma.so
#%{_includedir}/lzmalib.h

#%files static
#%defattr(644,root,root,755)
#%{_libdir}/liblzma.a
