%define _disable_lto 1
%define _disable_ld_no_undefined 1

# The stable 1.12 release is stuck on LLVM 14.
# Instead of backporting all the patches needed for newer versions,
# it's both faster and safer to use a 1.13 snapshot for the time being.
#define git 20240927

Name:		clazy
Summary:	Qt oriented code checker
Version:	1.15
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		https://invent.kde.org/sdk/clazy
Source0:	https://invent.kde.org/sdk/clazy/-/archive/%{version}/clazy-%{version}.tar.bz2
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Polly)
BuildRequires:	llvm-devel
BuildRequires:	clang-devel

%patchlist

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
