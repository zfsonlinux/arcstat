%global commit 0b4546e89ded86d2f11727d32fb1eb2caaf91ceb
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global repo_name arcstat

Name:           zfs-arcstat
Version:        0.5
Release:        1%{?dist}
Summary:        Perl script to read ZFS ARC kstat values
License:        GPLv2+
Group:          Applications/System
URL:            https://github.com/zfsonlinux/%{repo_name}
Source0:        https://github.com/zfsonlinux/%{repo_name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Sun::Solaris::Kstat)

%description
arcstat.pl is a Perl script that uses the Sun::Solaris::Kstat module to read
ZFS ARC kstat values from the system and report on an interval basis.

%prep
%setup -qn %{repo_name}-%{commit}

%build
# Do nothing

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p %{buildroot}%{_bindir}/
cp -p arcstat.pl %{buildroot}%{_bindir}/arcstat.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%attr(0755, root, root) %{_bindir}/arcstat.pl

%changelog
* Tue Jul 23 2013 Trey Dockendorf <treydock@gmail.com> 0.5-1
- Initial spec file creation
