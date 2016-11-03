%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name konstantin-fluentd
%global commit 0441f39ac3adcac403d0b71248274fb8f8c0a62e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-fluentd
Version:        0.7.0
Release:        1%{?alphatag}%{?dist}
Summary:        Installs, configures, and manages Fluentd data collector
License:        Apache-2.0

URL:            https://github.com/soylent/konstantin-fluentd

Source0:        https://github.com/soylent/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

#
# patches_base=v0.7.0
#

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
* Thu Nov 03 2016 Jon Schlueter <jschluet@redhat.com> 0.7.0-1
- Update to 0.7.0 (0441f39ac3adcac403d0b71248274fb8f8c0a62e)

* Tue Sep 20 2016 Haikel Guemar <hguemar@fedoraproject.org> - 0.6.1-1.0400aaf.git
- Newton update 0.6.1 (0400aafa8f23971485b838750d41928585cf3547)


