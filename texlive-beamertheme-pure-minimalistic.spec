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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The main features of this minimalistic Beamer theme are: Easily use own
logos. Customizable. Looks good in a 4:3 and 16:9 aspect ratio, without
the need to change anything. Provides an environment for vertically-
spaced items. Provides light and dark mode. Is designed to be purely
minimalistic without any distractions.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamertheme-pure-minimalistic
%dir %{_datadir}/texmf-dist/tex/latex/beamertheme-pure-minimalistic
%dir %{_datadir}/texmf-dist/doc/latex/beamertheme-pure-minimalistic/logos
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-pure-minimalistic/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-pure-minimalistic/README.md
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-pure-minimalistic/beamertheme-pure-minimalistic-demo.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-pure-minimalistic/beamertheme-pure-minimalistic-demo.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-pure-minimalistic/demo_bib.bib
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-pure-minimalistic/logos/header_logo.png
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-pure-minimalistic/logos/header_logo_darkmode.png
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-pure-minimalistic/logos/institute_logo.png
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-pure-minimalistic/logos/institute_logo_darkmode.png
%{_datadir}/texmf-dist/tex/latex/beamertheme-pure-minimalistic/beamercolorthemepureminimalistic.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-pure-minimalistic/beamerfontthemepureminimalistic.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-pure-minimalistic/beamerinnerthemepureminimalistic.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-pure-minimalistic/beamerouterthemepureminimalistic.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-pure-minimalistic/beamerthemepureminimalistic.sty
