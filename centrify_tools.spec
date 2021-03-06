%define name centrify_tools
%define version %VERSION%
%define release %RELEASE%
%define arch noarch
%define source https://github.com/mickep76/centrify_tools.git

%define buildroot %{_topdir}/BUILDROOT/

BuildRoot: %{buildroot}
Source: %{source}
Summary: Centrify Tools
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: System
AutoReqProv: no

%description
Tools for listing permissions and getting information for Centrify on the command line

%prep
mkdir -p %{buildroot}/usr/bin
mkdir %{buildroot}/usr/lib
mkdir %{buildroot}/etc
cp %{_topdir}/SOURCES/ad_group %{buildroot}/usr/bin
cp %{_topdir}/SOURCES/ad_host_roles %{buildroot}/usr/bin
cp %{_topdir}/SOURCES/ad_host_zone %{buildroot}/usr/bin
cp %{_topdir}/SOURCES/ad_zone_hosts %{buildroot}/usr/bin
cp %{_topdir}/SOURCES/ad_zone_roles %{buildroot}/usr/bin
cp %{_topdir}/SOURCES/ad_zones %{buildroot}/usr/bin
cp %{_topdir}/SOURCES/ad_functions %{buildroot}/usr/lib
cp %{_topdir}/SOURCES/ad.conf %{buildroot}/etc

%files
%defattr(-,root,root)
%dir /usr/bin
%dir /usr/lib
/usr/bin/*
/usr/lib/*
%config(noreplace) /etc/ad.conf
