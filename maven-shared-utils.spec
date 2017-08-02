%{?scl:%scl_package maven-shared-utils}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}maven-shared-utils
Version:        3.1.0
Release:        4.1%{?dist}
Summary:        Maven shared utility classes
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-shared-utils
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(com.google.code.findbugs:jsr305)
BuildRequires:  %{?scl_prefix}mvn(commons-io:commons-io)
BuildRequires:  %{?scl_prefix}mvn(junit:junit)
BuildRequires:  %{?scl_prefix}mvn(org.apache.commons:commons-lang3)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-core)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  %{?scl_prefix}mvn(org.fusesource.jansi:jansi)
BuildRequires:  %{?scl_prefix}mvn(org.hamcrest:hamcrest-core)

%description
This project aims to be a functional replacement for plexus-utils in Maven.

It is not a 100% API compatible replacement though but a replacement with
improvements: lots of methods got cleaned up, generics got added and we dropped
a lot of unused code.

%package javadoc
Summary:        Javadoc for %{pkg_name}
    

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 3.1.0-4.1
- Automated package import and SCL-ization

* Mon Feb 13 2017 Michael Simacek <msimacek@redhat.com> - 3.1.0-4
- Regenerate BuildRequires

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 27 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.0-2
- Re-enable tests

* Fri Jul 22 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.0-0.1.RC
- Update to upstream version 3.1.0
- Temporarly disable tests

* Fri Jul 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.1-2
- Remove unneeded build-requires

* Thu Jun  2 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.1-1
- Update to upstream version 3.0.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 16 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.0-2
- Enable all tests

* Mon Oct 12 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.0-1
- Update to upstream version 3.0.0

* Mon Sep 21 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.9-1
- Update to upstream version 0.9

* Mon Jun 22 2015 Michal Srb <msrb@redhat.com> - 0.8-1
- Update to upstream release 0.8

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 24 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7-1
- Update to upstream version 0.7

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 24 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.6-1
- Update to upstream version 0.6

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.5-3
- Use Requires: java-headless rebuild (#1067528)

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.5-2
- Fix unowned directory

* Mon Dec 23 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.5-1
- Update to upstream version 0.5
- Remove patch for MSHARED-285 (accepted upstream)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Tomas Radej <tradej@redhat.com> - 0.4-1
- Updated to latest upstream version
- Fixed and reenabled tests

* Mon Apr 08 2013 Michal Srb <msrb@redhat.com> - 0.3-2
- Disable tests (they don't work with junit >= 4.11)

* Fri Mar 15 2013 Michal Srb <msrb@redhat.com> - 0.3-1
- Update to upstream version 0.3

* Tue Feb 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.2-4
- Build with xmvn

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0.2-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 16 2013 Tomas Radej <tradej@redhat.com> - 0.2-1
- Initial version
