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


%define snapshot 1

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
Version:	1.1.0
Release:	1
%endif
License:	BSD
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
%if %snapshot
Source0:	%{name}-%{version}.tar.xz
%else
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
%endif

BuildRequires:	pkgconfig(ecore) >= 1.0.0
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
Obsoletes:	%_lib}efreet0-devel

%description -n %{develname}
Efreet development headers and development libraries.

%prep
%if %snapshot
%setup -qn %{name}
%else
%setup -q
%endif

%build
%if %snapshot
NOCONFIGURE=yes ./autogen.sh
%endif

%configure2_5x \
	--disable-static

%make

%install
rm -fr %{buildroot}
%makeinstall_std

# Get rid of unneeded testing cruft.
rm -rf %{buildroot}%{_datadir}/%{name}

%files
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

