Name:       libogg
Summary:    The Ogg bitstream file format library
Version:    1.3.5
Release:    1
License:    BSD
URL:        https://github.com/sailfishos/libogg
Source0:    %{name}-%{version}.tar.bz2
Patch1:     0001-Update-minimum-cmake-version-from-3.0-to-3.6.patch
BuildRequires: cmake
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Libogg is a library for manipulating Ogg bitstream file formats.
Libogg supports both making Ogg bitstreams and getting packets from
Ogg bitstreams.


%package devel
Summary:    Files needed for development using libogg
Requires:   %{name} = %{version}-%{release}

%description devel
Libogg is a library used for manipulating Ogg bitstreams. The
libogg-devel package contains the header files and documentation
needed for development using libogg.


%package doc
Summary:    Documentation for the Ogg runtime library
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description doc
Documentation for developing applications with libogg


%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%cmake -DBUILD_SHARED_LIBS=1
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/libogg.so.*

%files devel
%doc AUTHORS CHANGES README.md
%dir %{_includedir}/ogg
%{_includedir}/ogg/ogg.h
%{_includedir}/ogg/os_types.h
%{_includedir}/ogg/config_types.h
%{_libdir}/libogg.so
%{_libdir}/cmake/Ogg/*.cmake
%{_libdir}/pkgconfig/ogg.pc

%files doc
%{_docdir}/%{name}
