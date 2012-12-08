%define major 1
%define libname %mklibname datrie %{major}
%define develname %mklibname datrie -d

Summary:	Double-array structure for representing trie
Name:		libdatrie
Version:	0.2.4
Release:	%mkrel 3
License:	LGPLv2+ and GPLv2+
Group:		System/Libraries
URL:		http://linux.thai.net
Source0:	ftp://linux.thai.net/pub/thailinux/software/libthai/%name-%version.tar.gz
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
%{_mandir}/man1/trietool*.1*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc README AUTHORS NEWS
%{_docdir}/%{name}/README.migration
%{_includedir}/datrie
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/pkgconfig/*
%{_datadir}/doc/datrie/


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.4-2mdv2011.0
+ Revision: 661454
- mass rebuild

* Mon Nov 29 2010 Funda Wang <fwang@mandriva.org> 0.2.4-1mdv2011.0
+ Revision: 602821
- new version 0.2.4

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-2mdv2011.0
+ Revision: 602534
- rebuild

* Tue Mar 02 2010 Emmanuel Andry <eandry@mandriva.org> 0.2.3-1mdv2010.1
+ Revision: 513653
- New version 0.2.3

* Sun Jun 21 2009 Frederik Himpe <fhimpe@mandriva.org> 0.2.2-2mdv2010.0
+ Revision: 387583
- Don't package trietool manpage twice
- Fix license
- Update to new version 0.2.2 (new major)
- Move documentation to -devel package

* Tue Apr 07 2009 Funda Wang <fwang@mandriva.org> 0.1.3-2mdv2009.1
+ Revision: 364589
- use configure2_5x

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.1.3-2mdv2009.0
+ Revision: 222531
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Feb 22 2008 Thierry Vignaud <tv@mandriva.org> 0.1.3-1mdv2008.1
+ Revision: 173838
- new release

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.1.2-2mdv2008.1
+ Revision: 150514
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Sep 05 2007 Thierry Vignaud <tv@mandriva.org> 0.1.2-1mdv2008.0
+ Revision: 80102
- include man pages
- new release

* Fri Aug 31 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-4mdv2008.0
+ Revision: 76971
- cleanup borked deps

* Fri Aug 31 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-3mdv2008.0
+ Revision: 76832
- new devel naming


* Mon Jan 22 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.1.1-2mdv2007.0
+ Revision: 111936
- rename a sub package in order to let libthai build

* Mon Jan 22 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.1.1-1mdv2007.1
+ Revision: 111850
- Import libdatrie

* Mon Jan 22 2007 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.1.1-1mdv2007.1
- initial release

