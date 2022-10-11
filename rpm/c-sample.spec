Name:       c-sample
Summary:    Sample app written in C
Version:    0
Release:    1
License:    BSD
URL:        https://www.github.com/sailfish/c-sample
Source0:    %{name}-%{version}.tar.bz2
BuildRequires: pkgconfig(ssu-sysinfo)

%description
Simple app written in C

%prep
%autosetup -p1 -n %{name}-%{version}

%build
cd src
make

%install
rm -rf %{buildroot}
cd src
DESTDIR=%{buildroot} make install

%files
%defattr(-,root,root,-)
%license LICENSE
%{_bindir}/c-sample
