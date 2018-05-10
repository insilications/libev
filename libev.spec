#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libev
Version  : 4.24
Release  : 3
URL      : http://dist.schmorp.de/libev/libev-4.24.tar.gz
Source0  : http://dist.schmorp.de/libev/libev-4.24.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: libev-lib
Requires: libev-doc
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
Patch1: 0001-pkg-include-headers.diff

%description
libev is a high-performance event loop/event model with lots of features.
(see benchmark at http://libev.schmorp.de/bench.html)

%package dev
Summary: dev components for the libev package.
Group: Development
Requires: libev-lib
Provides: libev-devel

%description dev
dev components for the libev package.


%package doc
Summary: doc components for the libev package.
Group: Documentation

%description doc
doc components for the libev package.


%package lib
Summary: lib components for the libev package.
Group: Libraries

%description lib
lib components for the libev package.


%prep
%setup -q -n libev-4.24
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1525295313
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1525295313
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libev/ev++.h
/usr/include/libev/ev.h
/usr/include/libev/event.h
/usr/lib64/libev.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libev.so.4
/usr/lib64/libev.so.4.0.0
