Name: ripgrep
Version: 0.7.1
Release: 1%{?dist}
Summary: A search tool that combines the usability of ag with the raw speed of grep
License: MIT or Unlicense
URL: https://github.com/BurntSushi/ripgrep
Source0: https://github.com/BurntSushi/ripgrep/archive/%{version}/ripgrep-%{version}.tar.gz
BuildRequires: cargo
%if 0%{?fedora} >= 24
ExclusiveArch: x86_64 i686 armv7hl
%else
ExclusiveArch: x86_64 aarch64
%endif


%description
ripgrep is a command line search tool that combines the usability of The Silver
Searcher (an ack clone) with the raw speed of GNU grep. ripgrep is fast, cross
platform, and written in Rust.


%prep
%autosetup


%build
cargo build --release


%install
install -D -p -m 755 target/release/rg %{buildroot}%{_bindir}/rg
install -D -p -m 644 doc/rg.1 %{buildroot}%{_mandir}/man1/rg.1
install -D -p -m 644 target/release/build/ripgrep-*/out/rg.bash-completion %{buildroot}%{_datadir}/bash-completion/completions/rg
install -D -p -m 644 target/release/build/ripgrep-*/out/rg.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/rg.fish
install -D -p -m 644 complete/_rg %{buildroot}%{_datadir}/zsh/site-functions/_rg


%check
cargo test


%files
%license COPYING LICENSE-MIT UNLICENSE
%doc README.md CHANGELOG.md
%{_bindir}/rg
%{_mandir}/man1/rg.1*
%{_datadir}/bash-completion
%{_datadir}/fish
%{_datadir}/zsh


%changelog
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