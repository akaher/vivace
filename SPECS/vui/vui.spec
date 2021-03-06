Summary:	Metapackage for Vivace User Interface
Name:		vui
Version:	0.1
Release:	1
License:	Apache License
Group:		System Environment/Base
URL:		http://photon.org
Source:		%{name}-%{version}.tar.xz
%define sha1 vui=b82907f114c8bd81e6b7676a56fbe9d9977494ea
Vendor:		VMware, Inc.
Distribution:	Photon
Provides:	vui
BuildArch:	noarch
Requires:	linux-drivers-gpu lxde-common lxdm alsa-utils lxterminal firefox thunderbird gpicview grdesktop lxtask nemiver anjuta pidgin monodevelop pinta tomboy gpicview hicolor-icon-theme banshee gtkmm gvfs open-vm-tools >= 10.0.0-256

%description
Metapackage for Vivace User Interface.

%prep
%setup -q

%build

%install
find -type d -exec install -d {,%{buildroot}/}{} \;
find -type f -exec install -D -m 644 {,%{buildroot}/}{} \;

%clean
rm -rf $RPM_BUILD_ROOT

%post
#copy skel to root home folder
mkdir -p /root/.config
cp -a /etc/skel/.config/cairo-dock /root/.config/ 
cp -a /etc/skel/.config/pcmanfm /root/.config/

%files
%{_sysconfdir}/skel/.config/*
%{_datadir}
