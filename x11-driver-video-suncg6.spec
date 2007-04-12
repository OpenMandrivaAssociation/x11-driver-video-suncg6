Name: x11-driver-video-suncg6
Version: 1.1.0
Release: %mkrel 1
Summary: The X.org driver for sun cg6 Cards
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-suncg6-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for sun cg6 Cards


%prep
%setup -q -n xf86-video-suncg6-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/suncg6_drv.la
%{_libdir}/xorg/modules/drivers/suncg6_drv.so
%{_mandir}/man4/suncg6.4.bz2


