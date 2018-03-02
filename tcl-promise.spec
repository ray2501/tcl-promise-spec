#
# spec file for package tcl-promise
#

%define tarname promise

Name:           tcl-promise
Version:        1.0.3
Release:        0
License:        BSD-2-License
Summary:        The promise module for Tcl
Url:            http://tcl-promise.magicsplat.com/
Group:          Development/Languages/Tcl
Source:         %{tarname}-%{version}.tar.gz
BuildArch:      noarch
Requires:       tcl >= 8.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Promises are concurrency primitives that let you write asynchronous code
in a sequential style. This Tcl based implementation is mostly modeled on
the Javascript/ECMAScript standard.

%prep
%setup -q -n %{tarname}-%{version}

%build

%install
mkdir -p %{buildroot}%_datadir/tcl/%{tarname}%{version}
cp promise-1.0.3.tm %{buildroot}%_datadir/tcl/%{tarname}%{version}

cat > %{buildroot}%_datadir/tcl/%{tarname}%{version}/pkgIndex.tcl << 'EOD'
#
# Tcl package index file
#
package ifneeded promise 1.0.3 \
    [list source [file join $dir promise-1.0.3.tm]]
EOD

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%_datadir/tcl

%changelog
