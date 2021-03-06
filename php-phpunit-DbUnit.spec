%define		status		stable
%define		pearname	DbUnit
Summary:	DbUnit port for PHP/PHPUnit
Name:		php-phpunit-%{pearname}
Version:	1.3.1
Release:	2
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	ab9477d04b83b9d76d784fb2b5cb4319
URL:		https://github.com/sebastianbergmann/phpunit/
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.9.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(pdo)
Requires:	php(reflection)
Requires:	php(simplexml)
Requires:	php(spl)
Requires:	php-channel(pear.phpunit.de)
Requires:	php-pear
Requires:	php-symfony2-Yaml >= 2.1.0
Requires:	phpunit >= 3.7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DbUnit port for PHP/PHPUnit to support database interaction testing.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

mv docs/DbUnit/Samples examples

%build
packagexml2cl package.xml > ChangeLog

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
