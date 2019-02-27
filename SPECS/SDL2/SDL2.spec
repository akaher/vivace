Summary:        Simple DirectMedia Layer
Name:           SDL2
Version:        2.0.9
Release:        1%{?dist}
License:        zlib
URL:            http://www.libsdl.org/
Vendor:		VMware, Inc.
Distribution:	Photon

Source0: http://www.libsdl.org/release/%{name}-%{version}.tar.gz
%define sha1 SDL2=4354c6baad9a48486182656a7506abfb63e9bff5
# 9382b0b5a88767283dca8481bfddf23c75b3db1b
Group: System Environment/Libraries
BuildRequires: libXext-devel libX11-devel
# BuildRequires: libGL-devel libGLU-devel
BuildRequires: libXrender-devel libXrandr-devel 
# gettext-devel
BuildArch:      aarch64

%define __soext so

%description
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

%package devel
Summary: Libraries, includes and more to develop SDL applications.
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

This is the libraries, include files and other resources you can use
to develop SDL applications.


%prep
%setup -q 

%build
%configure
make %{?_smp_mflags}

%install
%makeinstall
rm -rf %{buildroot}/usr/lib/cmake/SDL2/sdl2-config.cmake

%files
%defattr(-,root,root)
%doc README*.txt COPYING.txt CREDITS.txt BUGS.txt
%{_libdir}/lib*.%{__soext}.*

%files devel
%defattr(-,root,root)
%doc docs/README*.md
%{_bindir}/*-config
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.%{__soext}
%{_includedir}/*/*.h
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*

%changelog
*   Mon Oct 22 2018 Ajay Kaher <akaher@vmware.com> 2.0.6-1
-   Adding BuildArch
