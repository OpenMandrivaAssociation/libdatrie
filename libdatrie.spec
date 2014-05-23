%define	major	1
%define	libname	%mklibname datrie %{major}
%define	devname	%mklibname datrie -d

Summary:	Double-array structure for representing trie
Name:		libdatrie
Version:	0.2.6
Release:	9
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
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

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
%{_datadir}/doc/datrie/


%changelog
* Sat Dec 07 2013 Bernhard Rosenkraenzer <bero@bero.eu> 0.2.6-9
+ Revision: c761612
- MassBuild#289: Increase release tag

* Sat Dec 07 2013 Bernhard Rosenkraenzer <bero@bero.eu> 0.2.6-8
+ Revision: 916bdec
- MassBuild#289: Increase release tag

* Sat Dec 07 2013 Bernhard Rosenkraenzer <bero@bero.eu> 0.2.6-7
+ Revision: c3242a5
- MassBuild#289: Increase release tag

* Sat Dec 07 2013 Bernhard Rosenkraenzer <bero@bero.eu> 0.2.6-6
+ Revision: f221af6
- MassBuild#289: Increase release tag

* Wed Oct 16 2013 Tomasz Paweł Gajc <phenomenal@wp.pl> 0.2.6-5
+ Revision: 58d77c3
- MassBuild#232: Increase release tag

* Wed Oct 16 2013 Tomasz Paweł Gajc <phenomenal@wp.pl> 0.2.6-4
+ Revision: 8e482c9
- MassBuild#232: Increase release tag

* Wed Oct 16 2013 Tomasz Paweł Gajc <phenomenal@wp.pl> 0.2.6-3
+ Revision: b497273
- MassBuild#232: Increase release tag

* Wed Oct 16 2013 Tomasz Paweł Gajc <phenomenal@wp.pl> 0.2.6-2
+ Revision: 06246ae
- MassBuild#232: Increase release tag

* Tue May 28 2013 mdawkins (Matthew Dawkins) <mattydaw@gmail.com> 0.2.6-1
+ Revision: 35525ff
- cleaned up spec

* Mon Feb 25 2013 Per Øyvind Karlsen (proyvind) <peroyvind@mandriva.org> 0.2.6-1
+ Revision: 7eb3020
- new version

* Wed Mar 07 2012 peroyvind <peroyvind@mandriva.org> 0.2.5-1
+ Revision: f2943f5
- drop useless dependency on pkgconfig
- SILENT: svn-revision: 782851

* Wed Mar 07 2012 peroyvind <peroyvind@mandriva.org> 0.2.5-1
+ Revision: 0b0c96a
- remove provides on %{name} for library package
- SILENT: svn-revision: 782837

* Wed Mar 07 2012 peroyvind <peroyvind@mandriva.org> 0.2.5-1
+ Revision: 536e8e8
- use %{EVRD} macro
- SILENT: svn-revision: 782834

* Wed Mar 07 2012 peroyvind <peroyvind@mandriva.org> 0.2.5-1
+ Revision: c457598
- cleanups
- SILENT: svn-revision: 782829

* Wed Mar 07 2012 peroyvind <peroyvind@mandriva.org> 0.2.5-1
+ Revision: 32f72c3
- new version
- SILENT: svn-revision: 782826

* Mon May 02 2011 oden <oden@mandriva.org> 0.2.4-2
+ Revision: c265290
- - mass rebuild
- SILENT: svn-revision: 661454

* Mon Nov 29 2010 fwang <fwang@mandriva.org> 0.2.4-1
+ Revision: 447a25d
- new version 0.2.4
- SILENT: svn-revision: 602821

* Sun Nov 28 2010 oden <oden@mandriva.org> 0.2.3-2
+ Revision: db81462
- - rebuild
- SILENT: svn-revision: 602534

* Tue Mar 02 2010 eandry <eandry@mandriva.org> 0.2.3-1
+ Revision: d06ff49
- New version 0.2.3
- SILENT: svn-revision: 513653

* Sun Jun 21 2009 fhimpe <fhimpe@mandriva.org> 0.2.2-2
+ Revision: 40310b3
- - Don't package trietool manpage twice
- - Fix license
- SILENT: svn-revision: 387583

* Sun Jun 21 2009 fhimpe <fhimpe@mandriva.org> 0.2.2-1
+ Revision: fae8fea
- - Update to new version 0.2.2 (new major)
- - Move documentation to -devel package
- SILENT: svn-revision: 387582

* Tue Apr 07 2009 fwang <fwang@mandriva.org> 0.1.3-2
+ Revision: 9bce989
- use configure2_5x
- SILENT: svn-revision: 364589

* Tue Jun 17 2008 tv <tv@mandriva.org> 0.1.3-2
+ Revision: 5707693
- rebuild
- SILENT: svn-revision: 222531

* Mon Jun 09 2008 pixel <pixel@mandriva.org> 0.1.3-1
+ Revision: debe906
- do not call ldconfig in %post/%postun, it is now handled by filetriggers
- SILENT: svn-revision: 217188

* Fri Feb 22 2008 tv <tv@mandriva.org> 0.1.3-1
+ Revision: 1edf82c
- new release
- SILENT: svn-revision: 173838

* Sun Jan 13 2008 tv <tv@mandriva.org> 0.1.2-2
+ Revision: e9ce912
- rebuild
- SILENT: svn-revision: 150514

* Fri Dec 21 2007 blino <blino@mandriva.org> 0.1.2-1
+ Revision: 5ca701e
- restore BuildRoot
- SILENT: svn-revision: 136549

* Mon Dec 17 2007 tv <tv@mandriva.org> 0.1.2-1
+ Revision: e50ea34
- kill re-definition of %buildroot on Pixel's request
- SILENT: svn-revision: 128504

* Wed Sep 05 2007 tv <tv@mandriva.org> 0.1.2-1
+ Revision: 3bdf95c
- include man pages
- SILENT: svn-revision: 80102


