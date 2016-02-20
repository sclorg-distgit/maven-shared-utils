%global pkg_name maven-shared-utils
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        0.4
Release:        3.11%{?dist}
Summary:        Maven shared utility classes
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-shared-utils
Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip
# Patching tests so that they are compatible with JUnit 4.11
# (upstream bug http://jira.codehaus.org/browse/MSHARED-285)
Patch0:         %{pkg_name}-tests.patch

BuildArch:      noarch

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  maven30-apache-commons-lang3
BuildRequires:  maven30-apache-rat
BuildRequires:  maven30-maven-shared
BuildRequires:  maven30-maven-shade-plugin
BuildRequires:  maven30-jsr-305

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
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%patch0 -p1
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%{_javadir}/%{pkg_name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 0.4-3.11
- maven33 rebuild

* Thu Jan 15 2015 Michal Srb <msrb@redhat.com> - 0.4-3.10
- Fix directory ownership

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 0.4-3.9
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 0.4-3.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.4-3.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.4-3.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.4-3.5
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.4-3.4
- Add missing BR: jsr-305

* Mon Feb 17 2014 Michal Srb <msrb@redhat.com> - 0.4-3.3
- SCL-ize BR/R

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.4-3.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.4-3.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.4-3
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.4-2
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

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

