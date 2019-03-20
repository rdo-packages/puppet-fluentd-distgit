%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name konstantin-fluentd
%global commit 4dfc15a70970fc9e182c876d6dc74b3764fbea4b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-fluentd
Version:        0.10.0
Release:        2%{?alphatag}%{?dist}
Summary:        Installs, configures, and manages Fluentd data collector
License:        ASL 2.0

URL:            https://github.com/soylent/konstantin-fluentd

Source0:        https://github.com/soylent/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

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
* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 0.10.0-2.4dfc15agit
- Update to post 0.10.0 (4dfc15a70970fc9e182c876d6dc74b3764fbea4b)



