#
# Conditional build:
%bcond_with	tests		# unit tests (hang?)
#
Summary:	AWS C Event Stream library
Summary(pl.UTF-8):	Biblioteka AWS C Event Stream
Name:		aws-c-event-stream
Version:	0.5.4
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/awslabs/aws-c-event-stream/releases
Source0:	https://github.com/awslabs/aws-c-event-stream/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	95eb544bb70beb39e53dd2f760f8ef12
URL:		https://github.com/awslabs/aws-c-event-stream
BuildRequires:	aws-c-common-devel
BuildRequires:	aws-c-io-devel
BuildRequires:	aws-checksums-devel
BuildRequires:	cmake >= 3.9
BuildRequires:	gcc >= 5:3.2
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C99 implementation of the vnd.amazon.event-stream content-type.

%description -l pl.UTF-8
Implementacja C99 typu treści vnd.amazon.event-stream.

%package devel
Summary:	Header files for AWS C Event Stream library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AWS C Event Stream
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	aws-c-io-devel
Requires:	aws-checksums-devel

%description devel
Header files for AWS C Event Stream library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AWS C Event Stream.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%if %{with tests}
%{__make} test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NOTICE README.md
%attr(755,root,root) %{_libdir}/libaws-c-event-stream.so.1.0.0

%files devel
%defattr(644,root,root,755)
%doc docs/images
%{_libdir}/libaws-c-event-stream.so
%{_includedir}/aws/event-stream
%{_libdir}/cmake/aws-c-event-stream
