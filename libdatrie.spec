%define	major	1
%define	libname	%mklibname datrie %{major}
%define	devname	%mklibname datrie -d

Summary:	Double-array structure for representing trie
Name:		libdatrie
Version:	0.2.12
Release:	1
License:	LGPLv2+ and GPLv2+
Group:		System/Libraries
Url:		http://linux.thai.net
Source0:	ftp://linux.thai.net/pub/thailinux/software/libthai/%{name}-%{version}.tar.xz
BuildRequires:	doxygen
BuildRequires:	pkgconfig

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
Provides:	%{name} = %{EVRD}

%description -n	trietool
Trietool is a trie manipulation tool.

%package -n	%{libname}
Summary:	Double-array structure for representing trie



Group:		System/Libraries

%description -n	%{libname}
This is an implementation of double-array structure for representing trie.

Trie is a kind of digital search tree, an efficient indexing method with
O(1) time complexity for searching. Comparably as efficient as hashing,
trie also provides flexibility on incremental matching and key spelling
manipulation. This makes it ideal for lexical analyzers, as well as spelling
dictionaries.

%package -n	%{devname}
Summary:	Double-array structure for representing trie



Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	datrie-devel = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{devname}
This package includes the header files and developer docs for the libdatrie
package.

%prep
%setup -q

%build
%configure \
	--disable-static
%make

%install
%makeinstall_std

rm -rf %{buildroot}%{_datadir}/doc/datrie/html

%files -n trietool
%{_bindir}/trietool*
%{_mandir}/man1/trietool*.1*

%files -n %{libname}
%{_libdir}/libdatrie.so.%{major}*

%files -n %{devname}
%doc README AUTHORS NEWS
%{_docdir}/%{name}/README.migration
%{_includedir}/datrie
%{_libdir}/libdatrie.so
%{_libdir}/pkgconfig/*
