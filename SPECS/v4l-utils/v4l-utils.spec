
Summary:        Utilities for video4linux and DVB devices
Name:           v4l-utils
Version:        1.16.3
Release:        1%{?dist}
License:        GPLv2+ and GPLv2
URL:            http://www.linuxtv.org/downloads/v4l-utils/
Group:          Applications/System
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        http://linuxtv.org/downloads/v4l-utils/v4l-utils-%{version}.tar.bz2
%define sha1 v4l-utils=63e79c846001bcd77c46acebfcebea1f441e32d7
# Source1:        qv4l2.desktop
# Source2:        qv4l2.svg
# BuildRequires:  l kernel-headers desktop-file-utils
# For /etc/udev/rules.d ownership
# Requires:       udev
# Requires:       libv4l = %{version}-%{release}
BuildArch:      aarch64

%description
v4l-utils is a collection of various video4linux (V4L) and DVB utilities. The
main v4l-utils package contains cx18-ctl, ir-keytable, ir-ctl, ivtv-ctl,
v4l2-ctl and v4l2-sysfs-path.

%package devel
Summary: Header and library files for v4l2
Group: Applications/System
Requires: %{name} = %{version}-%{release}
%description devel
These are the header and library files of util-linux.

%prep
%setup -q

%build
./bootstrap.sh
./configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}/lib/udev/rc_keymaps
rm -rf %{buildroot}/usr/local/etc/rc_maps.cfg
rm -rf %{buildroot}/usr/local/share
# %post -n libv4l -p /sbin/ldconfig
# %postun -n libv4l -p /sbin/ldconfig

%files
%defattr(-,root,root)
/lib/udev/rules.d/70-infrared.rules
/usr/local/bin/*
/usr/local/sbin/*
/usr/local/lib/libv4l/*
/usr/local/lib/*

%files devel
%defattr(-,root,root)
/usr/local/include/*

%changelog
*   Mon Feb 04 2019 Ajay Kaher <akaher@vmware.com> 1.16.3-1
-   Initial build.  First version


