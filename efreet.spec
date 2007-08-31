%define	name efreet
%define	version 0.0.3.006
%define release %mkrel 1

%define major 1
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: 	Enlightened efreet
Name: 		%{name}
Version: 	%{version}
Epoch:          1
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://www.get-e.org/
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot

BuildRequires: 	ecore-devel >= 0.9.9.038
BuildRequires:	multiarch-utils

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
Provides: efreet = %{version}-%{release}
Provides: %{libname} = %{version}-%{release}

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

%package -n %{libname}-devel
Summary: Enlightened efreet Library headers and development libraries
Group: System/Libraries
Requires: %{libname} = %{version}
Provides: %{libname}-devel = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{libname}-devel
Efreet development headers and development libraries.

%prep
%setup -q

%build
%configure2_5x

%make

%install
rm -fr %buildroot
%makeinstall

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/*
#%_datadir/doc/%{libname}-%version/*
%_datadir/%name/*

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_libdir}/*.so.%{major}*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_libdir}/lib*.*a
%{_includedir}/%name/*.h
%{_libdir}/pkgconfig/*
