#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libaom
Version  : 1
Release  : 4
URL      : https://aomedia.googlesource.com/aom/+archive/refs/heads/master.tar.gz
Source0  : https://aomedia.googlesource.com/aom/+archive/refs/heads/master.tar.gz
Summary  : GoogleTest (with main() function)
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libaom-bin = %{version}-%{release}
Requires: libaom-lib = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : nasm
BuildRequires : nasm-bin
BuildRequires : perl
BuildRequires : python3

%description
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

%package bin
Summary: bin components for the libaom package.
Group: Binaries

%description bin
bin components for the libaom package.


%package dev
Summary: dev components for the libaom package.
Group: Development
Requires: libaom-lib = %{version}-%{release}
Requires: libaom-bin = %{version}-%{release}
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
%setup -q -c -n master.tar
cd %{_builddir}/master.tar

%build
## build_prepend content
find . -type f -name 'link.txt' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name 'cmake_link_script' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name 'CMakeLists' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name '*.cmake' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name '*.make' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name 'flags.make' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name 'link.txt' -exec sed -i 's/\-fPIE/ /g' {} \;
find . -type f -name 'cmake_link_script' -exec sed -i 's/\-fPIE/ /g' {} \;
find . -type f -name 'CMakeLists' -exec sed -i 's/\-fPIE/ /g' {} \;
find . -type f -name '*.cmake' -exec sed -i 's/\-fPIE/ /g' {} \;
find . -type f -name '*.make' -exec sed -i 's/\-fPIE/ /g' {} \;
find . -type f -name 'flags.make' -exec sed -i 's/\-fPIE/ /g' {} \;
## build_prepend end
unset http_proxy
unset https_proxy
unset no_proxy
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587618310
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
export CFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=6 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-semantic-interposition -fno-plt -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe"
export FCFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=6 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-semantic-interposition -fno-plt -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe"
export FFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=6 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-semantic-interposition -fno-plt -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe"
export CFFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=6 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-semantic-interposition -fno-plt -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe"
export LDFLAGS="-O3 -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=6 -fno-semantic-interposition -fno-plt -fno-stack-protector -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native"
export CXXFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=6 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-semantic-interposition -fno-plt -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -fvisibility-inlines-hidden -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe"
export CCACHE_DISABLE=1
## altflags1 end
%cmake .. -DCMAKE_POSITION_INDEPENDENT_CODE=OFF -DSTATIC_LINK_CRT:BOOL=ON -DCMAKE_C_FLAGS_RELWITHDEBINFO="-O3 -g" -DCMAKE_CXX_FLAGS_RELWITHDEBINFO="-O3 -g" -DCMAKE_C_FLAGS_RELEASE="-O3 -g" -DCMAKE_CXX_FLAGS_RELEASE="-O3 -g" -DBUILD_STATIC_LIBS:BOOL=ON -DBUILD_STATIC_LIBS=1 -DENABLE_SHARED:bool=ON -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS:bool=ON -DCONFIG_AV1_ENCODER=1 -DENABLE_DOCS=0 -DENABLE_TESTS=0 -DENABLE_NASM=1 -DENABLE_NASM=ON -DCONFIG_RUNTIME_CPU_DETECT=1 -DCMAKE_INSTALL_LIBDIR=lib64
## make_prepend content
find . -type f -name 'link.txt' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name 'cmake_link_script' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name '*.cmake' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name '*.make' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name 'flags.make' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name 'link.txt' -exec sed -i 's/\-fPIE/ /g' {} \;
find . -type f -name 'cmake_link_script' -exec sed -i 's/\-fPIE/ /g' {} \;
find . -type f -name '*.cmake' -exec sed -i 's/\-fPIE/ /g' {} \;
find . -type f -name '*.make' -exec sed -i 's/\-fPIE/ /g' {} \;
find . -type f -name 'flags.make' -exec sed -i 's/\-fPIE/ /g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's/cmake_check_build_system/ /g' {} \;
## make_prepend end
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1587618310
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/aomdec
/usr/bin/aomenc

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
/usr/lib64/pkgconfig/aom.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libaom.so
/usr/lib64/libaom.so.0
/usr/lib64/libaom.so.1.0.0

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libaom.a
