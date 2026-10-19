%global forgeurl https://github.com/linuxmint/xviewer

Name:           xviewer
Version:        3.4.17
Release:        1%{?dist}
Summary:        Fast and functional image viewer

License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  yelp-tools
BuildRequires:  desktop-file-utils
BuildRequires:  cmake

BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libpeas1-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  libpeas-devel
BuildRequires:  cinnamon-desktop-devel
BuildRequires:  xapps-devel
BuildRequires:  libxml2-devel
BuildRequires:  zlib-devel
BuildRequires:  libX11-devel
BuildRequires:  gobject-introspection-devel

BuildRequires:  exempi-devel
BuildRequires:  libexif-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  lcms2-devel
BuildRequires:  librsvg2-devel

%description
Xviewer is a fast and functional image viewer developed by the
Linux Mint project. It supports image viewing, zooming, printing,
and various image metadata features.

%prep
%autosetup -n xviewer-%{version}

%build
%meson \
  -Ddocs=false
%meson_build

%install
%meson_install

%find_lang xviewer

%check
%meson_test

%files -f xviewer.lang
%license COPYING
%doc README.md AUTHORS THANKS MAINTAINERS
%{_bindir}/xviewer
%{_libdir}/xviewer/
%{_libdir}/pkgconfig/xviewer.pc
%{_includedir}/xviewer/
%{_datadir}/applications/xviewer.desktop
%{_datadir}/metainfo/xviewer.appdata.xml
%{_datadir}/glib-2.0/schemas/org.x.viewer.gschema.xml
%{_datadir}/glib-2.0/schemas/org.x.viewer.enums.xml
%{_datadir}/icons/hicolor/
%{_datadir}/xviewer/
%{_datadir}/help/

%changelog
* Mon Oct 19 2026 jarsxk <jarsxk@gmail.com> - 3.4.17-1
- Initial COPR package
