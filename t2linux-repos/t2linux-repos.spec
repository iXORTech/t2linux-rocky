Name: t2linux-repos
Version: 3.0.0
Release: 1%{?dist}
Summary: Copr repo for t2linux owned by iXOR Technology (Qubik65536).
License: MIT
URL: https://copr.fedorainfracloud.org/coprs/ixortech/t2linux

Provides: copr-ixortech-t2linux-release = 2.0.0-1
Obsoletes: copr-ixortech-t2linux-release < 1.0.0-2
Obsoletes: t2linux-repo < 7.0.0-2

Source0: copr-ixortech-t2linux.repo

%description
Patched kernel and supporting packages for hardware enablement on t2
macs.

%prep

%build

%install
install -D -m 644 %{SOURCE0} %{buildroot}/etc/yum.repos.d/copr-ixortech-t2linux.repo
	
%files
/etc/yum.repos.d/copr-ixortech-t2linux.repo
