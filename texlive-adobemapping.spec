%global tl_name adobemapping
%global tl_revision 66552

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Adobe cmap and pdfmapping files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/adobemapping
License:	bsd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adobemapping.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package comprises the collection of CMap and PDF mapping files made
available for distribution by Adobe.

