#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/efreet efreet; \
#cd efreet; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
#cd ..; \
#tar -Jcf efreet-$PKG_VERSION.tar.xz efreet/ --exclude .svn --exclude .*ignore


%define snapshot 0

%if %snapshot
%define	svndate	20120103
%define	svnrev	66149
%endif

%define	major 1
%define	libname %mklibname %{name} %major
%define	develname %mklibname %{name} -d

Summary: 	Enlightened efreet
Name:		efreet
Epoch:		2
%if %snapshot
Version:	1.1.99.%{svnrev}
Release:	0.%{svndate}.1
%else
Version:	1.7.3
Release:	1
%endif
License:	BSD
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
%if %snapshot
Source0:	%{name}-%{version}.tar.xz
%else
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.gz
%endif

BuildRequires:	pkgconfig(ecore) >= 1.7.0
BuildRequires:	pkgconfig(ecore-file) >= 1.7.0
BuildRequires:	pkgconfig(eet) >= 1.7.0
BuildRequires:	pkgconfig(eina) >= 1.7.0
Conflicts:	%{libname} < 2:1.1.99.66149-0.20120103.1

%description
An implementation of several specifications from freedesktop.org intended
for use in Enlightenment DR17 (e17) and other applications using the
Enlightenment Foundation Libraries (EFL). Currently, the following 
specifications are included:
  o Base Directory
  o Desktop Entry
  o Icon Theme
  o Menu

%package -n %{libname}
Summary:	Enlightened efreet Libraries
Group:		System/Libraries

%description -n %{libname}
Efreet libraries

An implementation of several specifications from freedesktop.org intended
for use in Enlightenment DR17 (e17) and other applications using the
Enlightenment Foundation Libraries (EFL). Currently, the following 
specifications are included:
  o Base Directory
  o Desktop Entry
  o Icon Theme
  o Menu

%package -n %{develname}
Summary:	Enlightened efreet Library headers and development libraries
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{_lib}efreet0-devel < 2:1.7.0

%description -n %{develname}
Efreet development headers and development libraries.

%prep
%if %{snapshot}
%setup -qn %{name}
%else
%setup -q
%endif

%build
%if %{snapshot}
NOCONFIGURE=yes ./autogen.sh
%endif

%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

# Get rid of unneeded testing cruft.
rm -rf %{buildroot}%{_datadir}/%{name}

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/%{name}*
%{_libexecdir}/%{name}/%{name}_desktop_cache_create
%{_libexecdir}/%{name}/%{name}_icon_cache_create

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/%{name}*



%changelog
* Tue Jun 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 2:1.2.0-1
+ Revision: 807058
- version update 1.2.0

* Wed Jan 04 2012 Matthew Dawkins <mattydaw@mandriva.org> 2:1.1.99.66149-0.20120103.1
+ Revision: 755650
- new version/snapshot 1.1.99.66149
- cleaned up spec and merged with Unity Linux spec
- disabled static build

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 2:1.0.1-1
+ Revision: 681652
- update to new version 1.0.1

* Sat Jan 29 2011 Funda Wang <fwang@mandriva.org> 2:1.0.0-1
+ Revision: 633928
- 1.0.0 final

* Sat Dec 18 2010 Funda Wang <fwang@mandriva.org> 2:1.0.0-0.beta3.1mdv2011.0
+ Revision: 622800
- 1.0 beta3

* Tue Nov 16 2010 Funda Wang <fwang@mandriva.org> 2:1.0.0-0.beta2.1mdv2011.0
+ Revision: 597954
- new version 1.0.0 beta2

* Wed Oct 13 2010 Funda Wang <fwang@mandriva.org> 2:1.0.0-0.beta.1mdv2011.0
+ Revision: 585313
- 1.0.0 beta

* Sat Jul 10 2010 Funda Wang <fwang@mandriva.org> 2:0.5.0.49898-1mdv2011.0
+ Revision: 550184
- New version 0.5.0.49898

* Sun Dec 13 2009 Funda Wang <fwang@mandriva.org> 2:0.5.0.063-1mdv2010.1
+ Revision: 478154
- new version 0.5.0.063

* Fri Aug 07 2009 Funda Wang <fwang@mandriva.org> 2:0.5.0.062-1mdv2010.0
+ Revision: 411122
- new version 0.5.0.062

* Wed Jul 08 2009 Funda Wang <fwang@mandriva.org> 2:0.5.0.061-3mdv2010.0
+ Revision: 393390
- rebuild

* Mon Jul 06 2009 Funda Wang <fwang@mandriva.org> 2:0.5.0.061-2mdv2010.0
+ Revision: 392829
- rebuild for new ecore

* Wed Jul 01 2009 Frederik Himpe <fhimpe@mandriva.org> 2:0.5.0.061-1mdv2010.0
+ Revision: 391346
- update to new version 0.5.0.061

* Sat May 02 2009 Funda Wang <fwang@mandriva.org> 2:0.5.0.060-1mdv2010.0
+ Revision: 370693
- New version 0.5.0.060

* Sun Mar 01 2009 Antoine Ginies <aginies@mandriva.com> 2:0.5.0.050-3mdv2009.1
+ Revision: 346322
- bump release
- SVN SNAPSHOT 20090227, release 0.5.0.050

* Sun Oct 12 2008 Funda Wang <fwang@mandriva.org> 2:0.5.0.050-1mdv2009.1
+ Revision: 292652
- New version 0.5.0.050

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2:0.5.0.043-3mdv2009.0
+ Revision: 266615
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jun 01 2008 Funda Wang <fwang@mandriva.org> 2:0.5.0.043-2mdv2009.0
+ Revision: 213991
- drop wrong provides

* Sun Jun 01 2008 Funda Wang <fwang@mandriva.org> 2:0.5.0.043-1mdv2009.0
+ Revision: 213989
- new devel package name
- New version 0.5.0.043

* Mon Feb 18 2008 Antoine Ginies <aginies@mandriva.com> 2:0.0.3.042-4mdv2008.1
+ Revision: 170090
- bump release

* Fri Feb 15 2008 Antoine Ginies <aginies@mandriva.com> 2:0.0.3.042-3mdv2008.1
+ Revision: 168998
- adjust buildrequires
- remove old source

* Sat Feb 02 2008 Austin Acton <austin@mandriva.org> 2:0.0.3.042-2mdv2008.1
+ Revision: 161520
- no major in devel package

* Sat Feb 02 2008 Austin Acton <austin@mandriva.org> 2:0.0.3.042-1mdv2008.1
+ Revision: 161499
- new version
- major decreases; bump epoch
- fix URL
- fix provides

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 10 2007 Austin Acton <austin@mandriva.org> 1:0.9.0.011-2mdv2008.1
+ Revision: 107469
- lib does not provide name

* Wed Oct 31 2007 Antoine Ginies <aginies@mandriva.com> 1:0.9.0.011-1mdv2008.1
+ Revision: 104096
- update tarball
- CVS SNAPSHOT 20071031, release 0.9.0.011

* Fri Aug 31 2007 Antoine Ginies <aginies@mandriva.com> 1:0.0.3.006-2mdv2008.0
+ Revision: 76718
- increase mkrel
- i should no disable ecore-desktop

* Fri Aug 31 2007 Antoine Ginies <aginies@mandriva.com> 1:0.0.3.006-1mdv2008.0
+ Revision: 76694
- fix missing libraries in package
- update to 0.0.3.006 efreet release
- CVS SNAPSHOT 20070830, release 0.0.1.005

* Wed Jun 13 2007 Antoine Ginies <aginies@mandriva.com> 1:0.0.3.002-8mdv2008.0
+ Revision: 38604
- CVS snapshot 20070613
- create category lists while scanning for .desktop files
- add efreet_menu_new()
- Init and shutdown util

* Mon Jun 04 2007 Antoine Ginies <aginies@mandriva.com> 1:0.0.3.002-7mdv2008.0
+ Revision: 35258
- CVS snapshot 20070605

* Mon Jun 04 2007 Thierry Vignaud <tv@mandriva.org> 1:0.0.3.002-6mdv2008.0
+ Revision: 35099
- fix major
- prevent major bug to happen again

* Wed May 30 2007 Antoine Ginies <aginies@mandriva.com> 1:0.0.3.002-5mdv2008.0
+ Revision: 32923
- increase mkrel
- fix provides

* Wed May 30 2007 Antoine Ginies <aginies@mandriva.com> 1:0.0.3.002-4mdv2008.0
+ Revision: 32781
- epoch strike back
- increase mkrel
- fix buildrequires, remove epoch

* Tue May 29 2007 Antoine Ginies <aginies@mandriva.com> 1:0.0.3.002-3mdv2008.0
+ Revision: 32628
- CVS SNAPSHOT 20070529, release 0.3.0.008

* Thu May 24 2007 Antoine Ginies <aginies@mandriva.com> 1:0.0.3.002-2mdv2008.0
+ Revision: 30645
- increase mkrel
- fix Builrequires

* Mon May 21 2007 Antoine Ginies <aginies@mandriva.com> 1:0.0.3.002-1mdv2008.0
+ Revision: 29104
- Import efreet

