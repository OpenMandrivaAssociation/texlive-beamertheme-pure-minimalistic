Name:		texlive-beamertheme-pure-minimalistic
Version:	56934
Release:	2
Summary:	A minimalistic presentation theme for LaTeX Beamer
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamertheme-pure-minimalistic
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-pure-minimalistic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-pure-minimalistic.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The main features of this minimalistic Beamer theme are: Easily
use own logos. Customizable. Looks good in a 4:3 and 16:9
aspect ratio, without the need to change anything. Provides an
environment for vertically-spaced items. Provides light and
dark mode. Is designed to be purely minimalistic without any
distractions.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/beamertheme-pure-minimalistic
%doc %{_texmfdistdir}/doc/latex/beamertheme-pure-minimalistic

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
