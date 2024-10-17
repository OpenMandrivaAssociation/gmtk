%define major	1
%define libname	%mklibname gmtk %{major}
%define libgmlib %mklibname gmlib %{major}
%define devname	%mklibname -d gmtk
%define _disable_rebuild_configure 1

Name:		gmtk
Summary:	Library for gnome-mplayer and gecko-mediaplayer
Version:	1.0.9
Release:	3
License: 	GPLv2+
Group:		System/Libraries
Url: 		https://code.google.com/p/gmtk/
Source0: 	http://gmtk.googlecode.com/files/%{name}-%{version}.tar.gz

BuildRequires: intltool
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libpulse-mainloop-glib)
BuildRequires: pkgconfig(x11)

%description
Library for gnome-mplayer and gecko-mediaplayer.

%package i18n
Summary:	Translation files for %{name}
Group:		System/Libraries
BuildArch:	noarch

%description i18n
This package contains translation files for %{name}.

%package -n	%{libname}
Summary:	Library for gnome-mplayer and gecko-mediaplayer
Group:		System/Libraries
Requires:	%{name}-i18n >= %{version}

%description -n	%{libname}
Library for gnome-mplayer and gecko-mediaplayer.

%package -n	%{libgmlib}
Summary:	Library for gnome-mplayer and gecko-mediaplayer
Group:		System/Libraries
Conflicts:	%{_lib}gmtk1 < 1.0.7-2

%description -n	%{libgmlib}
Library for gnome-mplayer and gecko-mediaplayer.

%package -n	%{devname}
Summary:	Libraries and include files for developing with libgmtk
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libgmlib} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package provides the necessary development libraries and include
files to allow you to develop with %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--enable-gsettings
%make

%install
%makeinstall_std
%find_lang %{name}

rm -f %{buildroot}%{_datadir}/doc/%{name}/*

%files i18n -f %{name}.lang

%files -n %{libname}
%{_libdir}/libgmtk.so.%{major}*

%files -n %{libgmlib}
%{_libdir}/libgmlib.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/*.pc
