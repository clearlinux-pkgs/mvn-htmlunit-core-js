#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-htmlunit-core-js
Version  : 2.17
Release  : 2
URL      : https://github.com/HtmlUnit/htmlunit-core-js/archive/core-js-2.17.tar.gz
Source0  : https://github.com/HtmlUnit/htmlunit-core-js/archive/core-js-2.17.tar.gz
Source1  : https://repo1.maven.org/maven2/net/sourceforge/htmlunit/htmlunit-core-js/2.17/htmlunit-core-js-2.17.jar
Source2  : https://repo1.maven.org/maven2/net/sourceforge/htmlunit/htmlunit-core-js/2.17/htmlunit-core-js-2.17.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : MPL-2.0
Requires: mvn-htmlunit-core-js-data = %{version}-%{release}

%description
This project is a Rhino fork, maintained to support features needed by HtmlUnit.

%package data
Summary: data components for the mvn-htmlunit-core-js package.
Group: Data

%description data
data components for the mvn-htmlunit-core-js package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/sourceforge/htmlunit/htmlunit-core-js/2.17
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/net/sourceforge/htmlunit/htmlunit-core-js/2.17

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/sourceforge/htmlunit/htmlunit-core-js/2.17
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/net/sourceforge/htmlunit/htmlunit-core-js/2.17


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/net/sourceforge/htmlunit/htmlunit-core-js/2.17/htmlunit-core-js-2.17.jar
/usr/share/java/.m2/repository/net/sourceforge/htmlunit/htmlunit-core-js/2.17/htmlunit-core-js-2.17.pom
