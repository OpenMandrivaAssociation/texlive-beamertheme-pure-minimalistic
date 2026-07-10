%global tl_name beamertheme-pure-minimalistic
%global tl_revision 56934

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0.0
Release:	%{tl_revision}.1
Summary:	A minimalistic presentation theme for LaTeX Beamer
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamertheme-pure-minimalistic
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-pure-minimalistic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-pure-minimalistic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The main features of this minimalistic Beamer theme are: Easily use own
logos. Customizable. Looks good in a 4:3 and 16:9 aspect ratio, without
the need to change anything. Provides an environment for vertically-
spaced items. Provides light and dark mode. Is designed to be purely
minimalistic without any distractions.

