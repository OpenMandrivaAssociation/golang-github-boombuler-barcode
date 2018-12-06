# https://github.com/boombuler/barcode
%global goipath         github.com/boombuler/barcode
Version:                1.0.0

%gometa

Name:           %{goname}
Release:        2%{?dist}
Summary:        A barcode creation lib for Go (Golang)
# Detected licences
# - Expat License at 'LICENSE'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

# Go 1.10 runs "go vet" by default, which triggers a few test failures.
# https://github.com/boombuler/barcode/pull/37
Patch0:         barcode-1.0.0-IntToRune-testfix.patch

%description
%{summary}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup -p1


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-2
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Ed Marshall <esm@logic.net> - 1.0.0-0
- Fix FTBFS, switch to release version number rather than git SHA.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170922git3cfea5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 08 2017 Ed Marshall <esm@logic.net> - 0-0.1.20170922git3cfea5a
- First package for Fedora
