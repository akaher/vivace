Summary:	FFmpeg is a solution to record, convert and stream audio and video
Name:		ffmpeg
Version:	3.4
Release:	3
License:	GPLv2
URL:		http://ffmpeg.org
Group:		System Environment/Multimedia
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ffmpeg.org/releases/ffmpeg-3.4.tar.xz
%define sha1 ffmpeg=af12e304da69dd54503901862f048677056f6f5a
BuildRequires:	git yasm x264-devel libva-devel alsa-lib-devel libvorbis-devel
BuildRequires:  pkg-config v4l-utils v4l-utils-devel
BuildRequires:  SDL2 SDL2-devel
Requires:	x264 libva alsa-lib libvorbis
%description
FFmpeg is a solution to record, convert and stream audio and video.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}-%{release}
Requires:	x264-devel libva-devel alsa-lib-devel libvorbis-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
git clone https://github.com/raspberrypi/userland.git
sed -i 's/-lflite"/-lflite -lasound"/' configure
./configure --extra-cflags="-I/usr/src/photon/BUILD/ffmpeg-3.4/userland/interface/vmcs_host/khronos/IL/" \
            --prefix=%{_prefix}  \
            --enable-gpl         \
            --enable-version3    \
            --enable-nonfree     \
            --disable-static     \
            --enable-shared      \
            --disable-debug      \
            --enable-libvorbis   \
            --enable-libx264     \
	    --enable-libv4l2	 \
	    --enable-omx	 \
	    --enable-omx-rpi	 \
	    --disable-stripping  \
            --docdir=/usr/share/doc/ffmpeg-3.4
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/ffmpeg/*
%{_mandir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_docdir}/*
%{_libdir}/pkgconfig/*

%changelog
*       Fri Feb 22 2019 Ajay Kaher <akaher@vmware.com> 3.4-3
-       Fix for RPi3
*	Tue Dec 05 2017 Alexey Makhalov <amakhalov@vmware.com> 3.4-1
-	initial version
