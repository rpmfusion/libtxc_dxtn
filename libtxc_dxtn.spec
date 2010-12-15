Name:           libtxc_dxtn
Version:        070518
Release:        1%{?dist}
Summary:        Free implementation of the s3tc texture compression algorithm

Group:          System Environment/Libraries
License:        BSD
URL:            http://people.freedesktop.org/~cbrill/libtxc_dxtn
Source0:        http://people.freedesktop.org/~cbrill/%{name}/%{name}%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  mesa-libGL-devel       

%description
Free implementation of the s3tc texture compression algorithm


%prep
%setup -q -n %{name}
sed -i -e 's|/usr/lib|%{_libdir}|g' Makefile
sed -i -e 's|pixerrorcolorbest\[3\]|pixerrorcolorbest[3]={0,0,0}|g' txc_compress_dxtn.c

%build
make %{?_smp_mflags} OPT_CFLAGS="%{optflags}"


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changelog
%{_libdir}/*.so

%changelog
* Tue Oct 26 2010 Hicham HAOUARI <hicham.haouari@gmail.com> - 070518-1
- Initial package for Fedora.
