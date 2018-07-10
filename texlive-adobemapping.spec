Name:		texlive-adobemapping
Version:	20180303
Release:	2
Summary:	Adobe cmap and pdfmapping files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/adobemapping
License:	BSD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adobemapping.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package comprises the collection of CMap and PDF mapping
files now made available for distribution by Adobe systems
incorporated.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/cmap/adobemapping

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts %{buildroot}%{_texmfdistdir}
