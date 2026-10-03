%define api 1
%define libname %mklibname ministream
%define develname %mklibname ministream -d

Name:           ministream
Version:        0.99.1
Release:        1
Summary:        Minimal (subset) AppStream metadata parser
Group:          System/Libraries
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/ministream
Source0:        https://gitlab.gnome.org/GNOME/ministream/-/archive/%{version}/ministream-%{version}.tar.bz2

BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(appstream)

%description
Ministream is a minimal subset of the AppStream metadata parser,
providing a lightweight library for parsing AppStream metadata.

%package -n %{libname}
Summary:        Runtime library for ministream
Group:          System/Libraries

%description -n %{libname}
Runtime library for ministream.

%package -n %{develname}
Summary:        Development files for ministream
Group:          Development/C
Requires:       %{libname} = %{EVRD}
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(gobject-2.0)

%description -n %{develname}
Development files for ministream, including headers and pkg-config
metadata.

%prep
%autosetup -p1

%build
%meson -Das-compare=disabled

%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/libministream.so.%{api}*
%{_libdir}/libministream.so.%{version}
%{_libdir}/girepository-1.0/Ministream-%{api}.typelib

%files -n %{develname}
%{_includedir}/ministream/
%{_libdir}/libministream.so
%{_libdir}/pkgconfig/ministream.pc
%{_datadir}/gir-1.0/Ministream-%{api}.gir
