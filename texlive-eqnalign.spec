Name:		texlive-eqnalign
Version:	43278
Release:	1
Summary:	Make eqnarray behave like align
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eqnalign
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqnalign.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqnalign.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqnalign.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package makes eqnarray environment behave like align from
amsmath'. It is intended for quick-fixing documents that use
eqnarray. In cases where it fails, manual conversion to align
is required, but these cases should be seldom.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/eqnalign
%{_texmfdistdir}/tex/latex/eqnalign
%doc %{_texmfdistdir}/doc/latex/eqnalign

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
