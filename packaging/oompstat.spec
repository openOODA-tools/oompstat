Name:           oompstat
Version:        0.1.0
Release:        1%{?dist}
Summary:        Per-core CPU utilization breakdown showing user, nice, system, irq, and idle time.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oompstat
Source0:        oompstat-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oompstat is a sovereign, capability-bounded CPU CORE METER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oompstat
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oompstat-uninstall

%files
/usr/bin/oompstat
/usr/bin/oompstat-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
