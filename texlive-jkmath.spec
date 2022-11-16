Name:		texlive-jkmath
Version:	47109
Release:	1
Summary:	Macros for mathematics that make the code more readable
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jkmath
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jkmath.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jkmath.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Inspired by the physicspackage on CTAN, the package defines
some simple macros for mathematical notation which make the
code more readable and/or allow flexibility in typesetting
material.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/jkmath
%doc %{_texmfdistdir}/doc/latex/jkmath

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
