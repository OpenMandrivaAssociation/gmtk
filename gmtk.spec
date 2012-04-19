%define major		0
%define libname		%mklibname gmtk %{major}
%define libnamedev	%mklibname -d gmtk

Name:		gmtk
Summary:	Library for gnome-mplayer and gecko-mediaplayer
Version:	1.0.6
Release:	%mkrel 1
License: 	GPLv2+
Group:		System/Libraries
Source0: 	http://gmtk.googlecode.com/files/%{name}-%{version}.tar.gz
URL: 		http://code.google.com/p/gmtk/
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libpulse-mainloop-glib)
BuildRequires: intltool

%description
Library for gnome-mplayer and gecko-mediaplayer.

%package i18n
Summary:	Translation files for %name
Group:		System/Libraries
BuildArch:	noarch

%description i18n
This package contains translation files for %name.

%package -n	%{libname}
Summary:	Library for gnome-mplayer and gecko-mediaplayer
Group:		System/Libraries
Requires:	%{name}-i18n

%description -n	%{libname}
Library for gnome-mplayer and gecko-mediaplayer.

%package -n	%{libnamedev}
Summary:	Libraries and include files for developing with libgmtk
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{libnamedev}
This package provides the necessary development libraries and include
files to allow you to develop with %{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static --enable-gsettings
make

%install
%makeinstall_std

%find_lang %name

rm -f %{buildroot}%{_libdir}/*.la %{buildroot}%{_datadir}/doc/%{name}/*

%files i18n -f %name.lang

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{libnamedev}
%{_libdir}/*.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/*.pc
