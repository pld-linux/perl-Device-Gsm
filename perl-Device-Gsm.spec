#
# Conditional build:
%bcond_with     tests   # perform "make test" (uses serial port)
#
%include        /usr/lib/rpm/macros.perl
%define pdir    Device
%define pnam    Gsm
Summary:        Device::Gsm - a Perl class for GSM
Summary(pl):    Device::Gsm - interface do obs�ugi GSM
Name:           perl-Device-Gsm
Version:        1.36
Release:        1
# same as perl
License:        GPL v1+ or Artistic
Group:          Development/Languages/Perl
Source0:        http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	61b72ca8775a18615c7c9877dcc733b5
BuildRequires:  perl-Device-Modem
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a perl extension to talk to GSM modems

%description -l pl
Jest to rozwini�cie modu�u do obs�ugi urz�dze� GSM

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
%{perl_vendorlib}/Device/Gsm/*.pm
%{perl_vendorlib}/Device/Gsm/Sms/*.pm
%{perl_vendorlib}/Device/Gsm/Sms/Token/*.pm

%{_mandir}/man3/*
