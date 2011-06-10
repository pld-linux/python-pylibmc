%define 	module	pylibmc
Summary:	Quick and small memcached cliend for Python
Summary(pl.UTF-8):	Mały i szybki klient memcsche dla Pythona
Name:		python-%{module}
Version:	1.1.1
Release:	0.1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	e43c54e285f8d937a3f1a916256ecc85
URL:		http://sendpatch.se/projects/pylibmc/
BuildRequires:	libmemcached-devel
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
#Requires:		python-libs
Requires:		python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pylibmc is a quick and small Python client for memcached written in C.

%description -l pl.UTF-8
pylibmc jest szybkim i małym klientem Pythona dla biblioteki
memcached napisanym w C.

%prep
%setup -q -n %{module}-%{version}

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python} setup.py build \
	--with-zlib

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO README* pooling.rst
%{py_sitedir}/*.py[co]
%attr(755,root,root) %{py_sitedir}/*.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/*.egg-info
%endif
