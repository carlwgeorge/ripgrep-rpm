Name: ripgrep
Version: 12.1.1
Release: 1%{?dist}
Summary: A search tool that combines the usability of ag with the raw speed of grep
License: MIT or Unlicense
URL: https://github.com/BurntSushi/ripgrep
Source0: https://github.com/BurntSushi/ripgrep/archive/%{version}/ripgrep-%{version}.tar.gz
BuildRequires: rust >= 1.34.0
BuildRequires: cargo
BuildRequires: asciidoc
%if 0%{?fedora} >= 24
ExclusiveArch: x86_64 i686 armv7hl
%else
ExclusiveArch: x86_64 aarch64
%endif


%description
ripgrep is a line-oriented search tool that recursively searches your current
directory for a regex pattern while respecting your gitignore rules.  ripgrep
is similar to other popular search tools like The Silver Searcher, ack and
grep.


%prep
%autosetup


%build
cargo build --release


%install
install -D -p -m 755 target/release/rg %{buildroot}%{_bindir}/rg
install -D -p -m 644 target/release/build/ripgrep-*/out/rg.1 %{buildroot}%{_mandir}/man1/rg.1
install -D -p -m 644 target/release/build/ripgrep-*/out/rg.bash %{buildroot}%{_datadir}/bash-completion/completions/rg
install -D -p -m 644 target/release/build/ripgrep-*/out/rg.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/rg.fish
install -D -p -m 644 complete/_rg %{buildroot}%{_datadir}/zsh/site-functions/_rg


%check
cargo test


%files
%license COPYING LICENSE-MIT UNLICENSE
%doc README.md CHANGELOG.md GUIDE.md FAQ.md
%{_bindir}/rg
%{_mandir}/man1/rg.1*
%{_datadir}/bash-completion
%{_datadir}/fish
%{_datadir}/zsh


%changelog
* Thu Dec 31 2020 Konstantin Glukhov <konstantin@konstantin.computer> - 12.1.1-1
- Latest upstream

* Mon Jun 10 2019 Carl George <carl@george.computer> - 11.0.1-1
- Latest upstream

* Mon Sep 10 2018 Carl George <carl@george.computer> - 0.10.0-1
- Latest upstream

* Mon Aug 06 2018 Carl George <carl@george.computer> - 0.9.0-1
- Latest upstream

* Sat Mar 03 2018 Carl George <carl@george.computer> - 0.8.1-1
- Latest upstream

* Tue Feb 13 2018 Carl George <carl@george.computer> - 0.8.0-1
- Latest upstream
- Man page is now generated during build
- Bash completion filename updated
- Include new guide and FAQ files

* Tue Nov 07 2017 Carl George <carl@george.computer> - 0.7.1-1
- Latest upstream

* Fri Jul 07 2017 Carl George <carl@george.computer> - 0.5.2-1
- Latest upstream
- Add zsh and fish completions

* Mon Apr 24 2017 Carl George <carl.george@rackspace.com> - 0.5.1-1
- Latest upstream

* Wed Mar 15 2017 Carl George <carl.george@rackspace.com> - 0.5.0-1
- Latest upstream

* Sun Dec 25 2016 Carl George <carl.george@rackspace.com> - 0.3.2-1
- Latest upstream
- Add bash completion
- Enable build for EPEL7 aarch64

* Sun Nov 27 2016 Carl George <carl.george@rackspace.com> - 0.3.1-1
- Latest upstream

* Sat Nov 12 2016 Carl George <carl.george@rackspace.com> - 0.2.9-1
- Latest upstream

* Mon Nov 07 2016 Carl George <carl.george@rackspace.com> - 0.2.8-1
- Latest upstream

* Thu Oct 13 2016 Carl George <carl.george@rackspace.com> - 0.2.3-1
- Latest upstream
- Set ExclusiveArch to match build requirements

* Thu Sep 29 2016 Carl George <carl.george@rackspace.com> - 0.2.1-1
- Initial spec file
