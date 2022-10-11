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
gcc -o c-sample c-sample.c -lssusysinfo

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m755 src/c-sample %{buildroot}%{_bindir}

%files
%defattr(-,root,root,-)
%license LICENSE
%{_bindir}/c-sample
