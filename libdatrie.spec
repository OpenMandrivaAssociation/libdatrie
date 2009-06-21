%define major 1
%define libname %mklibname datrie %{major}
%define develname %mklibname datrie -d

Summary:	Double-array structure for representing trie
Name:		libdatrie
Version:	0.2.2
Release:	%mkrel 1
License:	LGPL
Group:		System/Libraries
URL:		http://linux.thai.net
Source0:	ftp://linux.thai.net/pub/thailinux/software/libthai/%name-%version.tar.gz
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	pkgconfig
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This is an implementation of double-array structure for representing trie.

Trie is a kind of digital search tree, an efficient indexing method with
O(1) time complexity for searching. Comparably as efficient as hashing,
trie also provides flexibility on incremental matching and key spelling
manipulation. This makes it ideal for lexical analyzers, as well as spelling
dictionaries.

%package -n	trietool
Summary:	Trie manipulation tool
Group:		Databases
Provides:	%{name} = %{version}

%description -n	trietool
Trietool is a trie manipulation tool.

%package -n	%{libname}
Summary:	Double-array structure for representing trie
Group:		System/Libraries
Provides:	%{name} = %{version}

%description -n	%{libname}
This is an implementation of double-array structure for representing trie.

Trie is a kind of digital search tree, an efficient indexing method with
O(1) time complexity for searching. Comparably as efficient as hashing,
trie also provides flexibility on incremental matching and key spelling
manipulation. This makes it ideal for lexical analyzers, as well as spelling
dictionaries.

%package -n	%{develname}
Summary:	Double-array structure for representing trie
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	pkgconfig
Provides:	datrie-devel = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname datrie 0 -d}

%description -n	%{develname}
This package includes the header files and developer docs for the libdatrie
package.

Install libdatrie-devel if you want to develop programs which will use
libdatrie.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

rm %{buildroot}%{_libdir}/*.la

%if %mdkversion < 200900
%post   -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n trietool
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc README AUTHORS COPYING NEWS
%{_docdir}/%{name}/README.migration
%{_includedir}/datrie
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/pkgconfig/*
%{_datadir}/doc/datrie/
%_mandir/man*/*
