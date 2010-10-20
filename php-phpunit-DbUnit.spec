%include	/usr/lib/rpm/macros.php
%define		status		stable
%define		pearname	DbUnit
Summary:	%{pearname} - DbUnit port for PHP/PHPUnit
Name:		php-phpunit-DbUnit
Version:	1.0.0
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	07b6b9d544c08b54aea840ed05a99ed0
URL:		http://pear.phpunit.de/package/DbUnit/
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.9.1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-channel(pear.phpunit.de)
Requires:	php-pear
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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}}
%pear_package_install
install -p usr/bin/* $RPM_BUILD_ROOT%{_bindir}

# don't care for tests
#rm -rf $RPM_BUILD_ROOT%{php_pear_dir}/tests/%{pearname}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc docs/DbUnit/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%attr(755,root,root) %{_bindir}/dbunit
%{php_pear_dir}/PHPUnit/Extensions/Database
