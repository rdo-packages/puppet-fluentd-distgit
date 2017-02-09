%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%define upstream_name konstantin-fluentd

Name:           puppet-fluentd
Version:        0.9.0
Release:        1%{?dist}
Summary:        Installs, configures, and manages Fluentd data collector
License:        ASL 2.0

URL:            https://github.com/soylent/konstantin-fluentd

Source0:        https://github.com/soylent/konstantin-fluentd/archive/v%{version}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Installs, configures, and manages Fluentd data collector

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/fluentd/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/fluentd/



%files
%{_datadir}/openstack-puppet/modules/fluentd/


%changelog
* Thu Feb 09 2016 Alfredo Moralejo <amoralej@redhat.com> 0.9.0-1
- Update to 0.9.0

