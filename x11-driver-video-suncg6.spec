ExclusiveArch:  sparc sparc64
Name: x11-driver-video-suncg6
Version: 1.1.1
Release: %mkrel 1
Summary: X.org driver for sun cg6 Cards
Group: System/X11
URL: https://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-suncg6-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-suncg6 is the X.org driver for sun cg6 Cards.

%prep
%setup -q -n xf86-video-suncg6-%{version}

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/suncg6_drv.la
%{_libdir}/xorg/modules/drivers/suncg6_drv.so
%{_mandir}/man4/suncg6.*
