%{!?python:%define python python}

Name:           %{python}-twisted
Version:        8.2.0
Release:        3.1%{?dist}
Summary:        Event-based framework for internet applications
Group:          Development/Libraries
License:        MIT
URL:            http://twistedmatrix.com/
Source:         README.fedora
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       %{python}-twisted-core   >= %{version}
Requires:       %{python}-twisted-conch  >= 8.2.0
Requires:       %{python}-twisted-lore   >= 8.2.0
Requires:       %{python}-twisted-mail   >= 8.2.0
Requires:       %{python}-twisted-names  >= 8.2.0
Requires:       %{python}-twisted-news   >= 8.2.0
Requires:       %{python}-twisted-runner >= 8.0.0
Requires:       %{python}-twisted-web    >= 8.2.0
Requires:       %{python}-twisted-words  >= 8.2.0
Obsoletes:      Twisted < 2.4.0-1
Provides:       Twisted = %{version}-%{release}
Obsoletes:      twisted < 2.4.0-1
Provides:       twisted = %{version}-%{release}

%description
Twisted is an event-based framework for internet applications.  It includes a
web server, a telnet server, a chat server, a news server, a generic client
and server for remote object access, and APIs for creating new protocols and
services. Twisted supports integration of the Tk, GTK+, Qt or wxPython event
loop with its main event loop. The Win32 event loop is also supported, as is
basic support for running servers on top of Jython.

Installing this package brings all Twisted sub-packages into your system.

%prep
%setup -c -T
install -p -m 0644 %{SOURCE0} README

%files
%defattr(-,root,root,-)
%doc README

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 8.2.0-3.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 29 2008 Matthias Saou <http://freshrpms.net/> 8.2.0-1
- Update to 8.2.0.
- Change back spec cosmetic details from Paul's to Thomas' preference.

* Wed Jul 16 2008 Matthias Saou <http://freshrpms.net/> 8.1.0-2
- Update to 8.1.0.
- Minor spec file cleanups.
- Merge back changes from Paul Howarth.

* Wed May 21 2008 Thomas Vander Stichele <thomas at apestaart dot org>
- 2.5.0-1
- update to 2.5.0 release (only the umbrella package was missing)

* Tue Jan 16 2007 Thomas Vander Stichele <thomas at apestaart dot org>
- 2.4.0-3
- list packages in README.fedora

* Wed Jan 03 2007 Thomas Vander Stichele <thomas at apestaart dot org>
- 2.4.0-2
- add a README.fedora
- made noarch, since it doesn't actually install any python twisted/ module
  code
- fixed provides/obsoletes

* Wed Jun 07 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 2.4.0-1
- this is now a pure umbrella package

* Mon Oct 10 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.1.0-1
- upstream release

* Tue Aug 23 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.0.1-1
- upstream release

* Mon Apr 04 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.0.0-2
- add zsh support

* Fri Mar 25 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.0.0-1
- final release

* Thu Mar 17 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.0.0-0.2.a3
- dropped web2

* Wed Mar 16 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.0.0-0.1.a3
- upstream release

* Sat Mar 12 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.0.0-0.1.a2
- new prerelease; FE versioning

* Mon Feb 07 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.0.0a1-1
- prep for split

* Fri Aug 20 2004 Jeff Pitman <symbiont+pyvault@berlios.de> 1.3.0-1
- new version

* Mon Apr 19 2004 Jeff Pitman <symbiont+pyvault@berlios.de> 1.2.0-3
- vaultize

* Mon Apr 12 2004 Jeff Pitman <symbiont+pyvault@berlios.de> 1.2.0-2
- require pyOpenSSL, SOAPpy, openssh-clients, crypto, dia so trial can run

