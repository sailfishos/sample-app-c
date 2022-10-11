Name:       sample-app-c
Summary:    Sample app written in C
Version:    0
Release:    1
License:    BSD
URL:        https://www.github.com/sailfish/sample-app-c
Source0:    %{name}-%{version}.tar.bz2
BuildRequires: pkgconfig(ssu-sysinfo)

%description
Simple app written in C

%prep
%autosetup -p1 -n %{name}-%{version}

%build
# If you need to pass arguments to make, replace "%make_build" with
# "make -C src". This will not be necessary with SDK release 3.10 and
# later.
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%license LICENSE
%{_bindir}/sample-app-c
