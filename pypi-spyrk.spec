#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-spyrk
Version  : 0.0.4
Release  : 29
URL      : https://files.pythonhosted.org/packages/6d/b9/8d168df047a4aa9318ab701fd8232f17ed0153ca5ba45685bb6fbb59319a/spyrk-0.0.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/6d/b9/8d168df047a4aa9318ab701fd8232f17ed0153ca5ba45685bb6fbb59319a/spyrk-0.0.4.tar.gz
Summary  : Python module for Spark devices
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: pypi-spyrk-license = %{version}-%{release}
Requires: pypi-spyrk-python = %{version}-%{release}
Requires: pypi-spyrk-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cached_property)
BuildRequires : pypi(hammock)
BuildRequires : pypi(mock)
Patch1: fixdeps.patch

%description
=====
        
        Python module for Spark devices.

%package license
Summary: license components for the pypi-spyrk package.
Group: Default

%description license
license components for the pypi-spyrk package.


%package python
Summary: python components for the pypi-spyrk package.
Group: Default
Requires: pypi-spyrk-python3 = %{version}-%{release}

%description python
python components for the pypi-spyrk package.


%package python3
Summary: python3 components for the pypi-spyrk package.
Group: Default
Requires: python3-core
Provides: pypi(spyrk)
Requires: pypi(cached_property)
Requires: pypi(hammock)
Requires: pypi(mock)

%description python3
python3 components for the pypi-spyrk package.


%prep
%setup -q -n spyrk-0.0.4
cd %{_builddir}/spyrk-0.0.4
%patch1 -p1
pushd ..
cp -a spyrk-0.0.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656369659
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-spyrk
cp %{_builddir}/spyrk-0.0.4/LICENSE %{buildroot}/usr/share/package-licenses/pypi-spyrk/84dca3c4c2a464f21963f4ebaefbd0042094d286
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-spyrk/84dca3c4c2a464f21963f4ebaefbd0042094d286

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
