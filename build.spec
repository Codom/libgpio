Name:          libgpiod
Version:       1.2.1
Release:       1%{?dist}
Summary:       C library and tools for interacting with linux GPIO char device

License:       LGPLv2+
URL:           https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/
Source0:       https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/snapshot/%{name}-%{version}.tar.gz

BuildRequires: automake autoconf autoconf-archive libtool
BuildRequires: doxygen
BuildRequires: gcc gcc-c++
BuildRequires: kernel-headers
BuildRequires: kmod-devel
BuildRequires: libstdc++-devel
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: systemd-devel

%description
libgpiod is a C library and tools for interacting with the linux GPIO character 
device (gpiod stands for GPIO device) The new character device interface 
guarantees all allocated resources are freed after closing the device file 
descriptor and adds several new features that are not present in the obsolete 
sysfs interface (like event polling, setting/reading multiple values at once or 
open-source and open-drain GPIOs).

%package utils
Summary: Utilities for GPIO
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Utilities for interacting with GPIO character devices.

%package c++
Summary: C++ bindings for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description c++
C++ bindings for use with %{name}.

%package -n python3-%{name}
Summary: Python 3 bindings for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Python 3 bindings for development with %{name}.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%prep
%autosetup

%build
autoreconf -vif
%configure --enable-tools=yes --disable-static --enable-tests \
           --enable-bindings-cxx --enable-bindings-python

%make_build

%install
%make_install

#Remove libtool archives.
find %{buildroot} -name '*.la' -delete


%ldconfig_scriptlets

%files
%license COPYING
%doc README
%{_libdir}/%{name}.so.*

%files utils
%{_bindir}/gpio*

%files c++
%{_libdir}/libgpiodcxx.so.*

%files -n python3-%{name}
%{python3_sitearch}/gpiod.so

%files devel
%{_includedir}/gpiod.*
%{_libdir}/pkgconfig/libgpiod*.pc
%{_libdir}/%{name}*.so

%changelog
* Sat Feb 16 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.1-1
- Update to 1.2.1 release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 10 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.2-1
- Update to 1.2 release

* Thu Jul 26 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.1-1
- Update to 1.1.1 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1-2
- Rebuilt for Python 3.7

* Thu May 17 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.1-1
- Update to 1.1 release
- New C++ and Python 3 bindings

* Sun Apr 15 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.1-1
- Update to 1.0.1

* Thu Feb  8 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.0-1
- Update to 1.0.0 with stable API

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov  9 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.2-1
- Update to 0.3.2

* Tue Aug 22 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.3-2
- Minor review updates

* Sat Jul  1 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.3-1
- Initial package

