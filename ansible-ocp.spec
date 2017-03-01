Summary: Ansible OCP Playbooks
Name:    ansible-ocp
Version: 1.1.0
Release: 1%{?dist}
Group:   Applications/System
License: GPLv3+ and ASL 2.0
URL: https://github.com/fusor/ansible-ocp
Source0:    %{name}-%{version}.tar.gz

BuildArch: noarch

Requires: ansible >= 2.1

%description
Ansible module for installing and configuring Openshift container platform.

%prep
%setup -q -n %{name}-%{version}
rm -rf ansible-ocp.spec rel-eng

%build

%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/%{name}
cp -r * %{buildroot}/%{_datadir}/%{name}

%files
%{_datadir}/%{name}

%changelog
