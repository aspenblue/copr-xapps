%global forgeurl https://github.com/xapp-project/xepub

Name:           xepub
Version:        1.0.2
Release:        1%{?dist}
Summary:        EPUB reader for Linux desktops

License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3
BuildRequires:  gettext
BuildRequires:  gtk-update-icon-cache
BuildRequires:  glib2-devel
BuildRequires:  meson >= 0.59.0
BuildRequires:  ninja-build
BuildRequires:  pkgconf-pkg-config


Requires:       gtk3
Requires:       webkit2gtk4.1
Requires:       python3
Requires:       python3-gobject
Requires:       python3-setproctitle
Requires:       python3-xapp
Requires:       xapp-symbolic-icons

%description
Xepub is a secure and comfortable EPUB reader for Linux desktops.
It is part of the XApp project and is designed to work across
different desktop environments and Linux distributions.

%prep
%autosetup -n xepub-%{version}

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install

%files
%license LICENSES/*
%doc README.md
%{_bindir}/xepub
%{_datadir}/applications/xepub.desktop
%{_datadir}/glib-2.0/schemas/org.x.xepub.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/xepub.svg
%{_datadir}/xepub/

%changelog
* Mon Oct 19 2026 jarsxk <jarsxk@gmail.com> - 1.0.2-1
- Initial COPR package
