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
cd src
gcc -o sample-app-c sample-app-c.c $(pkg-config --cflags --libs ssu-sysinfo)

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m755 src/sample-app-c %{buildroot}%{_bindir}

%files
%defattr(-,root,root,-)
%license LICENSE
%{_bindir}/sample-app-c
