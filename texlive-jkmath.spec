%global tl_name jkmath
%global tl_revision 47109

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Macros for mathematics that make the code more readable
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/jkmath
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jkmath.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jkmath.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Inspired by the physicspackage on CTAN, the package defines some simple
macros for mathematical notation which make the code more readable
and/or allow flexibility in typesetting material.

