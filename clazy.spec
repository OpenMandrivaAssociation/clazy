%define _disable_lto 1
%define _disable_ld_no_undefined 1

# The stable 1.11 release is stuck on LLVM 14.
# Instead of backporting all the patches needed for newer versions,
# it's both faster and safer to use a 1.12 snapshot for the time being.
%define git 20240127

Name:		clazy
Summary:	Qt oriented code checker
Version:	1.12
Release:	%{?git:0.%{git}.}2
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		https://invent.kde.org/sdk/clazy
Source0:	https://%{?git:invent.kde.org/sdk/clazy/-/archive/master/clazy-master.tar.bz2}%{!?git:download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz}
Patch:		clazy-llvm-18.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Polly)
BuildRequires:	llvm-devel
BuildRequires:	clang-devel

%description
Qt oriented code checker based on clang framework. 
Krazy's little brother. 

%prep
%autosetup -p1 %{?git:-n %{name}-master}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%if ! %{cross_compiling}
%check
cd build
export PATH=`pwd`/bin:$PATH
ctest || :
%endif

%files
%doc %{_docdir}/clazy/*
%{_bindir}/%{name}
%{_bindir}/%{name}-standalone
%{_libdir}/ClazyPlugin.so
%doc %{_mandir}/man1/%{name}.1*
%{_datadir}/metainfo/org.kde.clazy.metainfo.xml
