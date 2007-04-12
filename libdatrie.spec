%define major 0
%define libname %mklibname datrie %major

Summary: Double-array structure for representing trie
Name:    libdatrie
Version: 0.1.1
Release: %mkrel 2
License: LGPL
Group:   System/Libraries
URL:     http://linux.thai.net
Source0: ftp://linux.thai.net/pub/thailinux/software/libthai/%name-%version.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root

BuildRequires: pkgconfig doxygen
BuildRequires: automake libtool

%description

This is an implementation of double-array structure for representing trie.

Trie is a kind of digital search tree, an efficient indexing method with
O(1) time complexity for searching. Comparably as efficient as hashing,
trie also provides flexibility on incremental matching and key spelling
manipulation. This makes it ideal for lexical analyzers, as well as spelling
dictionaries.

%package -n trietool
Summary:  Trie manipulation tool
Group:    Databases
Provides: %name = %version

%description -n trietool
Trietool is a trie manipulation tool.


%package -n %libname
Summary:  Double-array structure for representing trie
Group:    System/Libraries
Provides: %name = %version

%description -n %libname
This is an implementation of double-array structure for representing trie.

Trie is a kind of digital search tree, an efficient indexing method with
O(1) time complexity for searching. Comparably as efficient as hashing,
trie also provides flexibility on incremental matching and key spelling
manipulation. This makes it ideal for lexical analyzers, as well as spelling
dictionaries.

%package -n %libname-devel

Summary:  Double-array structure for representing trie
Group:    Development/C
Requires: %{libname} = %{version}
Requires: pkgconfig
Provides: %name-devel = %version
Provides: datrie-devel = %version

%description -n %libname-devel
This package includes the header files and developer docs for the libdatrie
package.

Install libdatrie-devel if you want to develop programs which will use
libdatrie.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n trietool
%defattr(-, root, root)
%_bindir/*
%{_mandir}/man1/*

%files -n %libname
%defattr(-, root, root)
%doc README AUTHORS COPYING NEWS
%{_libdir}/lib*.so.%{major}*

%files -n %libname-devel
%defattr(-, root, root)
%{_includedir}/datrie
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/pkgconfig/*
%_datadir/doc/datrie/


