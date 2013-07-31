%define	major	1
%define	libname %mklibname %{name} %{major}
%define	devname %mklibname %{name} -d

Summary:	Enlightened efreet
Name:		efreet
Epoch:		2
Version:	1.7.8
Release:	1
License:	BSD
Group:		Graphical desktop/Enlightenment
Url:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.fr/releases/%{name}-%{version}.tar.bz2

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

%package -n %{devname}
Summary:	Enlightened efreet Library headers and development libraries
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Efreet development headers and development libraries.

%prep
%setup -q

%build
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
%{_libdir}/lib%{name}*.so.%{major}*

%files -n %{devname}
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/*
%{_includedir}/%{name}*

