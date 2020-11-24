%define _disable_lto 1
%define _disable_ld_no_undefined 1

Name:		clazy
Summary:	Qt oriented code checker
Version:	1.8
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		http://www.aelog.org/
Source0:	http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		0000-Fix-build-issues-using-llvm-10.0.0.patch
Patch1:		0001-Make-clazy-build-30-faster-by-using-precompiled-head.patch
Patch2:		1f2f7f47bc9a5bce6e3eaabbef8743f0617bc015.patch
BuildRequires:	cmake(ECM)
BuildRequires:	llvm-devel
BuildRequires:	clang-devel

%description
Qt oriented code checker based on clang framework. 
Krazy's little brother. 

%prep
%autosetup -p1 -c
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-standalone
%{_libdir}/ClazyPlugin.so
%{_mandir}/man1/%{name}.1*
%{_datadir}/metainfo/org.kde.clazy.metainfo.xml
%{_docdir}/clazy/*
