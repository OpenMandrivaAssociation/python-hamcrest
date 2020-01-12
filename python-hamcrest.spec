%bcond_without python2

Summary:	Hamcrest matchers for Python
Name:		python-hamcrest
Version:	1.10.0
Release:	1
Group:		Development/Python
License:	MIT
Url:		https://github.com/hamcrest/PyHamcrest
Source0:	https://github.com/hamcrest/PyHamcrest/archive/V%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3egg(setuptools)
BuildRequires:	python3egg(six)

%description
Matchers that can be combined to create flexible expressions of intent

%if %{with python2}
%package -n python2-hamcrest
Summary:	Hamcrest matchers for Python2
Group:		Development/Python
BuildRequires:	pkgconfig(python2)
BuildRequires:	pythonegg(setuptools)
BuildRequires:	pythonegg(six)

%description -n python2-hamcrest
Matchers that can be combined to create flexible expressions of intent
%endif

%prep
%setup -q -c

mv PyHamcrest-%{version} python2
cp -r python2 python3

%install
pushd python2
PYTHONDONTWRITEBYTECODE=yes python2 setup.py install --root %{buildroot}
popd

pushd python3
PYTHONDONTWRITEBYTECODE=yes python setup.py install --root %{buildroot}
popd

%files
%{py_puresitedir}/hamcrest
%{py_puresitedir}/PyHamcrest*py3*.egg-info

%if %{with python2}
%files -n python2-hamcrest
%{py2_puresitedir}/hamcrest
%{py2_puresitedir}/PyHamcrest*py2*.egg-info
%endif
