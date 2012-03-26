%define		status		stable
%define		pearname	DbUnit
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - DbUnit port for PHP/PHPUnit
Name:		php-phpunit-DbUnit
Version:	1.1.2
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	813ec72a4b9bee5c9eec326957846843
URL:		http://pear.phpunit.de/
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.9.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-channel(pear.phpunit.de)
Requires:	php-pdo
Requires:	php-pear
Requires:	php-phpunit-PHPUnit >= 3.6.0
Requires:	php-reflection
Requires:	php-simplexml
Requires:	php-spl
Requires:	php-symfony-YAML >= 1.0.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DbUnit port for PHP/PHPUnit

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

mv docs/DbUnit/Samples examples

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}}
%pear_package_install
install -p usr/bin/* $RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%attr(755,root,root) %{_bindir}/dbunit
%{php_pear_dir}/PHPUnit/Extensions/Database

%{_examplesdir}/%{name}-%{version}
