%define	name efreet
%define	version 0.0.3.042
%define release %mkrel 4

%define major 0
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
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires: 	ecore-devel => 0.9.9.042

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

%package -n %{libname}-devel
Provides: %{libname} = %{version}-%{release}
Summary: Enlightened efreet Library headers and development libraries
Group: System/Libraries
Requires: %{libname} = %{epoch}:%{version}
Provides: lib%{name}-devel = %{epoch}:%{version}-%{release}
Provides: %{name}-devel = %{epoch}:%{version}-%{release}

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
%_datadir/%name/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*
%{_libdir}/lib*_mime.so.0*


%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_libdir}/lib*.*a
%{_includedir}/%name/*.h
%{_libdir}/pkgconfig/*
