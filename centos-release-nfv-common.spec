Summary: Common release file to establish shared metadata for CentOS NFV SIG
Name: centos-release-nfv-common
Epoch: 0
Version: 1
Release: 5%{?dist}
License: GPL
Group: System Environment/Base
Source0: RPM-GPG-KEY-CentOS-SIG-NFV
Source1:CentOS-nfv-common.repo
URL: http://wiki.centos.org/SpecialInterestGroup/NFV
BuildArch: noarch

Provides: centos-release-nfv-common
Requires: centos-release-scl-rh

BuildRoot: %{_tmppath}/%{name}-root

%description
Common files needed by other centos-release components in the NFV SIG

%prep
%setup -q -n %{name} -T -c

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/pki/rpm-gpg/
install -m 644 %SOURCE0 $RPM_BUILD_ROOT/etc/pki/rpm-gpg/
install -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-nfv-common.repo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-NFV
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-nfv-common.repo

%changelog
* Sat Feb 2 2019 Thomas F Herbert <therbert@redhat.com> - 1-5
- Restored previous search path for testing repo.
* Fri Feb 1 2019 Thomas F Herbert <therbert@redhat.com> - 1-4
- Fixed bad search path in repo.
* Fri Nov 9 2018 Thomas F Herbert <therbert@redhat.com> - 1-3
- Added requirement for scl for devtoolset-7
* Wed Oct 31 2018 Thomas F Herbert <therbert@redhat.com> - 1-2
- Added nfv common repo
* Thu Mar 1 2018 Thomas F Herbert <therbert@redhat.com> - 1-1
- Basic setup with the gpg key
- Derived from the CentOS Virtualization SIG
