#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libaom
Version  : 2.0
Release  : 4
URL      : file:///insilications/build/clearlinux/packages/libaom/libaom-v2.0.tar.gz
Source0  : file:///insilications/build/clearlinux/packages/libaom/libaom-v2.0.tar.gz
Source1  : file:///insilications/build/clearlinux/packages/libaom/aom-testdata-clr-.tar.gz
Summary  : GoogleTest (with main() function)
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libaom-lib = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : ccache
BuildRequires : findutils
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : nasm
BuildRequires : nasm-bin
BuildRequires : perl
BuildRequires : pkg-config
BuildRequires : python3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Fix-best_encode.sh.patch
Patch2: 0002-Fix-tools_common.sh.patch

%description
=========
# AV1 Codec Library
## Contents
1. [Building the lib and applications](#building-the-library-and-applications)
- [Prerequisites](#prerequisites)
- [Get the code](#get-the-code)
- [Basics](#basic-build)
- [Configuration options](#configuration-options)
- [Dylib builds](#dylib-builds)
- [Debugging](#debugging)
- [Cross compiling](#cross-compiling)
- [Sanitizer support](#sanitizers)
- [MSVC builds](#microsoft-visual-studio-builds)
- [Xcode builds](#xcode-builds)
- [Emscripten builds](#emscripten-builds)
- [Extra Build Flags](#extra-build-flags)
- [Build with VMAF support](#build-with-vmaf)
2. [Testing the library](#testing-the-av1-codec)
- [Basics](#testing-basics)
- [Unit tests](#1_unit-tests)
- [Example tests](#2_example-tests)
- [Encoder tests](#3_encoder-tests)
- [IDE hosted tests](#ide-hosted-tests)
- [Downloading test data](#downloading-the-test-data)
- [Adding a new test data file](#adding-a-new-test-data-file)
- [Additional test data](#additional-test-data)
- [Sharded testing](#sharded-testing)
- [Running tests directly](#1_running-test_libaom-directly)
- [Running tests via CMake](#2_running-the-tests-via-the-cmake-build)
3. [Coding style](#coding-style)
4. [Submitting patches](#submitting-patches)
- [Login cookie](#login-cookie)
- [Contributor agreement](#contributor-agreement)
- [Testing your code](#testing-your-code)
- [Commit message hook](#commit-message-hook)
- [Upload your change](#upload-your-change)
- [Incorporating Reviewer Comments](#incorporating-reviewer-comments)
- [Submitting your change](#submitting-your-change)
- [Viewing change status](#viewing-the-status-of-uploaded-changes)
5. [Support](#support)
6. [Bug reports](#bug-reports)

%package dev
Summary: dev components for the libaom package.
Group: Development
Requires: libaom-lib = %{version}-%{release}
Provides: libaom-devel = %{version}-%{release}
Requires: libaom = %{version}-%{release}

%description dev
dev components for the libaom package.


%package lib
Summary: lib components for the libaom package.
Group: Libraries

%description lib
lib components for the libaom package.


%package staticdev
Summary: staticdev components for the libaom package.
Group: Default
Requires: libaom-dev = %{version}-%{release}

%description staticdev
staticdev components for the libaom package.


%prep
%setup -q -n libaom
cd %{_builddir}
tar xf %{_sourcedir}/aom-testdata-clr-.tar.gz
cd %{_builddir}/libaom
mkdir -p aom-testdata-clr/
cp -r %{_builddir}/aom-testdata-clr/* %{_builddir}/libaom/aom-testdata-clr/
%patch1 -p1
%patch2 -p1

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600338207
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
export CFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC"
# -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden -flto-partition=none
# gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common  -ffat-lto-objects
export CXXFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -fPIC"
#
export FCFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC"
export FFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC"
export CFFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC"
#
export LDFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC"
#
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%define _lto_cflags 1
#%define _lto_cflags %{nil}
#
# export PATH="/usr/lib64/ccache/bin:$PATH"
# export CCACHE_NOHASHDIR=1
# export CCACHE_DIRECT=1
# export CCACHE_SLOPPINESS=pch_defines,locale,time_macros
# export CCACHE_DISABLE=1
## altflags1 end
##
%define _lto_cflags 1
##
%cmake .. -DCONFIG_TUNE_VMAF=0 -DENABLE_SHARED:bool=ON -DCMAKE_BUILD_TYPE=Release -DCONFIG_AV1_ENCODER=1 -DENABLE_DOCS=0 -DENABLE_TESTS=0 -DENABLE_EXAMPLES=0 -DENABLE_NASM=1 -DENABLE_NASM=ON -DCMAKE_INSTALL_LIBDIR=lib64 -DBUILD_SHARED_LIBS=1
## make_prepend content
#find . -type f -name 'link.txt' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'cmake_link_script' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name '*.cmake' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name '*.make' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'flags.make' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1600338207
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/aom/aom.h
/usr/include/aom/aom_codec.h
/usr/include/aom/aom_decoder.h
/usr/include/aom/aom_encoder.h
/usr/include/aom/aom_frame_buffer.h
/usr/include/aom/aom_image.h
/usr/include/aom/aom_integer.h
/usr/include/aom/aomcx.h
/usr/include/aom/aomdx.h
/usr/lib64/libaom.so
/usr/lib64/pkgconfig/aom.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libaom.so.2
/usr/lib64/libaom.so.2.0.0

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libaom.a
