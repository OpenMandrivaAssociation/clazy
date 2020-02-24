%define _disable_lto 1
%define _disable_ld_no_undefined 1

Name:		clazy
Summary:	Qt oriented code checker
Version:	1.6
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		http://www.aelog.org/
Source0:	http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	llvm-devel
BuildRequires:	clang-devel

%description
Qt oriented code checker based on clang framework. 
Krazy's little brother. 

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

# manpage in wrong place
# looks like 1.4 fixed it
#mkdir -p %{buildroot}/%{_mandir}/man1
#mv %{buildroot}/%_prefix/man/man1/* %{buildroot}/%{_mandir}/man1

%files
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-standalone
%{_libdir}/ClangLazy.so
%{_mandir}/man1/%{name}.1*
#{_datadir}/%{name}
%{_docdir}/clazy/*
