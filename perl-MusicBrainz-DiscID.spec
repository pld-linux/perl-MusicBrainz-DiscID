#
# Conditional build:
%bcond_without	tests		# unit tests
#
%define		pdir	MusicBrainz
%define		pnam	DiscID
Summary:	MusicBrainz::DiscID - Perl interface for the MusicBrainz libdiscid library
Summary(pl.UTF-8):	MusicBrainz::DiscID - perlowy interfejs do biblioteki MusicBrainz libdiscid
Name:		perl-MusicBrainz-DiscID
Version:	0.06
Release:	1
License:	MIT
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MusicBrainz/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6579d43d270c965563f84fd5ffe0dde5
URL:		https://metacpan.org/dist/MusicBrainz-DiscID
BuildRequires:	libdiscid-devel >= 0.2.2
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig >= 1:0.11
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Pod >= 1.00
BuildRequires:	perl-Test-Simple
%endif
Requires:	libdiscid >= 0.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MusicBrainz::DiscID is a class to calculate a MusicBrainz DiscID 
from an audio CD in the drive. The coding style is slightly different
to the C interface to libdiscid, because it makes use of perl's Object
Oriented functionality.

%description -l pl.UTF-8
MusicBrainz::DiscID to klasa do obliczania MusicBrainz DiscID z płyty
CD Audio w czytniku. Styl kodowania różni się nieco od interfejsu C do
libdiscid, ponieważ wykorzystuje perlowe programowanie zorientowane
obiektowo.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -pr examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%dir %{perl_vendorarch}/MusicBrainz
%{perl_vendorarch}/MusicBrainz/DiscID.pm
%dir %{perl_vendorarch}/auto/MusicBrainz
%dir %{perl_vendorarch}/auto/MusicBrainz/DiscID
%attr(755,root,root) %{perl_vendorarch}/auto/MusicBrainz/DiscID/DiscID.so
%{_mandir}/man3/MusicBrainz::DiscID.3pm*
%{_examplesdir}/%{name}-%{version}
