Name:		sedlabanki-getcurrency
Version:	1.0.3
Release:	1%{?dist}
Summary:	Fetch currency rates via sedlabanki xml interface

Group:		Applications/System
License:	GPLv3
URL:		https://github.com/opinkerfi/%{name}
Source0:	%{name}-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch



%description
Fetches groupmebers from a Active Directory server and outputs require statements
needed for authentication.

%clean
rm -rf $RPM_BUILD_ROOT

%prep
%setup -q


%build
true


%install
test "x$RPM_BUILD_ROOT" != "x" && rm -rf $RPM_BUILD_ROOT
install -D -m 755 %{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}

%files
%doc README.md gpl-3.0.txt
%{_bindir}/%{name}



%changelog

