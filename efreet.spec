%define	name efreet
%define	version 1.0.0
%define release %mkrel -c beta3 1

%define major 1
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary: 	Enlightened efreet
Name: 		%{name}
Version: 	%{version}
Epoch:          2
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://www.enlightenment.org/
Source: 	http://download.enlightenment.org/releases/%{name}-%{version}.beta3.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires: 	ecore-devel >= 1.0.0

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
Summary: Enlightened efreet Libraries
Group: System/Libraries

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

%package -n %libnamedev
Summary: Enlightened efreet Library headers and development libraries
Group: System/Libraries
Requires: %{libname} = %{epoch}:%{version}
Provides: lib%{name}-devel = %{epoch}:%{version}-%{release}
Provides: %{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes: %mklibname efreet 0 -d

%description -n %libnamedev
Efreet development headers and development libraries.

%prep
%setup -qn %{name}-%{version}.beta3

%build
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/*
%{_libexecdir}/efreet/efreet_desktop_cache_create
%_datadir/%name/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_libdir}/lib*.*a
%{_includedir}/*
%{_libdir}/pkgconfig/*
