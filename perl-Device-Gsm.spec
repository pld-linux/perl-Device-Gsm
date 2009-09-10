#
# Conditional build:
%bcond_with	tests	# perform "make test" (uses serial port)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Device
%define		pnam	Gsm
Summary:	Device::Gsm - a Perl class for GSM
Summary(pl.UTF-8):	Device::Gsm - perlowy interfejs do obsługi GSM
Name:		perl-Device-Gsm
Version:	1.54
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Device/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	897e7e1b8e00d755b17b66f4ee159251
URL:		http://search.cpan.org/dist/Device-Gsm/
BuildRequires:	perl-Device-Modem
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Perl extension to talk to GSM modems.

%description -l pl.UTF-8
Jest to rozszerzenie Perla do obsługi modemów GSM.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_vendorlib}/Device/*.pm
%dir %{perl_vendorlib}/Device/Gsm
%{perl_vendorlib}/Device/Gsm/*.pm
%dir %{perl_vendorlib}/Device/Gsm/Sms
%{perl_vendorlib}/Device/Gsm/Sms/*.pm
%dir %{perl_vendorlib}/Device/Gsm/Sms/Token
%{perl_vendorlib}/Device/Gsm/Sms/Token/*.pm
%{_mandir}/man3/*
