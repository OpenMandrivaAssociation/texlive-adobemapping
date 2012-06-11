# revision 26261
# category Package
# catalog-ctan /support/adobemapping
# catalog-date 2012-05-08 12:38:17 +0200
# catalog-license bsd
# catalog-version undef
Name:		texlive-adobemapping
Version:	20120508
Release:	1
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
%{_texmfdistdir}/fonts/cmap/adobemapping/LICENSE
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/90ms-RKSJ-UCS2
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/90pv-RKSJ-UCS2
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/90pv-RKSJ-UCS2C
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/Adobe-CNS1-B5pc
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/Adobe-CNS1-ETen-B5
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/Adobe-CNS1-H-CID
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/Adobe-CNS1-H-Host
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/Adobe-CNS1-H-Mac
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/Adobe-GB1-GBK-EUC
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/Adobe-GB1-GBpc-EUC
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/Adobe-GB1-H-CID
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/Adobe-GB1-H-Host
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/Adobe-GB1-H-Mac
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/Adobe-Japan1-90ms-RKSJ
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/Adobe-Japan1-90pv-RKSJ
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/Adobe-Japan1-H-CID
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/Adobe-Japan1-H-Host
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/Adobe-Japan1-H-Mac
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/Adobe-Japan1-PS-H
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/Adobe-Japan1-PS-V
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/Adobe-Korea1-H-CID
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/Adobe-Korea1-H-Host
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/Adobe-Korea1-H-Mac
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/Adobe-Korea1-KSCms-UHC
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/Adobe-Korea1-KSCpc-EUC
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/B5pc-UCS2
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/B5pc-UCS2C
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/ETen-B5-UCS2
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/GBK-EUC-UCS2
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/GBpc-EUC-UCS2
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/GBpc-EUC-UCS2C
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/KSCms-UHC-UCS2
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/KSCpc-EUC-UCS2
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/KSCpc-EUC-UCS2C
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/UCS2-90ms-RKSJ
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/UCS2-90pv-RKSJ
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/UCS2-B5pc
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/UCS2-ETen-B5
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/UCS2-GBK-EUC
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/UCS2-GBpc-EUC
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/UCS2-KSCms-UHC
%{_texmfdistdir}/fonts/cmap/adobemapping/MappingOther/UCS2-KSCpc-EUC
%{_texmfdistdir}/fonts/cmap/adobemapping/README
%{_texmfdistdir}/fonts/cmap/adobemapping/ToUnicode/Adobe-CNS1-UCS2
%{_texmfdistdir}/fonts/cmap/adobemapping/ToUnicode/Adobe-GB1-UCS2
%{_texmfdistdir}/fonts/cmap/adobemapping/ToUnicode/Adobe-Japan1-UCS2
%{_texmfdistdir}/fonts/cmap/adobemapping/ToUnicode/Adobe-Korea1-UCS2
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/Adobe-CNS1-0
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/Adobe-CNS1-1
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/Adobe-CNS1-2
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/Adobe-CNS1-3
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/Adobe-CNS1-4
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/Adobe-CNS1-5
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/Adobe-CNS1-6
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/B5-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/B5-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/B5pc-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/B5pc-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/CNS-EUC-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/CNS-EUC-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/CNS1-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/CNS1-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/CNS2-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/CNS2-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/ETHK-B5-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/ETHK-B5-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/ETen-B5-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/ETen-B5-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/ETenms-B5-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/ETenms-B5-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/HKdla-B5-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/HKdla-B5-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/HKdlb-B5-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/HKdlb-B5-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/HKgccs-B5-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/HKgccs-B5-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/HKm314-B5-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/HKm314-B5-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/HKm471-B5-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/HKm471-B5-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/HKscs-B5-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/HKscs-B5-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/UniCNS-UCS2-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/UniCNS-UCS2-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/UniCNS-UTF16-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/UniCNS-UTF16-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/UniCNS-UTF32-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/UniCNS-UTF32-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/UniCNS-UTF8-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/CMap/UniCNS-UTF8-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ac16/cid2code.txt
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/Adobe-GB1-0
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/Adobe-GB1-1
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/Adobe-GB1-2
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/Adobe-GB1-3
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/Adobe-GB1-4
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/Adobe-GB1-5
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/GB-EUC-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/GB-EUC-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/GB-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/GB-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/GBK-EUC-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/GBK-EUC-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/GBK2K-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/GBK2K-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/GBKp-EUC-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/GBKp-EUC-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/GBT-EUC-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/GBT-EUC-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/GBT-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/GBT-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/GBTpc-EUC-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/GBTpc-EUC-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/GBpc-EUC-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/GBpc-EUC-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/UniGB-UCS2-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/UniGB-UCS2-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/UniGB-UTF16-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/UniGB-UTF16-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/UniGB-UTF32-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/UniGB-UTF32-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/UniGB-UTF8-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/CMap/UniGB-UTF8-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ag15/cid2code.txt
%{_texmfdistdir}/fonts/cmap/adobemapping/ai0/CMap/Identity-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ai0/CMap/Identity-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/78-EUC-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/78-EUC-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/78-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/78-RKSJ-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/78-RKSJ-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/78-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/78ms-RKSJ-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/78ms-RKSJ-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/83pv-RKSJ-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/90ms-RKSJ-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/90ms-RKSJ-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/90msp-RKSJ-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/90msp-RKSJ-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/90pv-RKSJ-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/90pv-RKSJ-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/Add-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/Add-RKSJ-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/Add-RKSJ-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/Add-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/Adobe-Japan1-0
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/Adobe-Japan1-1
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/Adobe-Japan1-2
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/Adobe-Japan1-3
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/Adobe-Japan1-4
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/Adobe-Japan1-5
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/Adobe-Japan1-6
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/EUC-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/EUC-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/Ext-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/Ext-RKSJ-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/Ext-RKSJ-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/Ext-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/Hankaku
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/Hiragana
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/Katakana
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/NWP-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/NWP-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/RKSJ-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/RKSJ-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/Roman
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/UniJIS-UCS2-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/UniJIS-UCS2-HW-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/UniJIS-UCS2-HW-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/UniJIS-UCS2-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/UniJIS-UTF16-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/UniJIS-UTF16-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/UniJIS-UTF32-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/UniJIS-UTF32-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/UniJIS-UTF8-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/UniJIS-UTF8-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/UniJIS2004-UTF16-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/UniJIS2004-UTF16-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/UniJIS2004-UTF32-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/UniJIS2004-UTF32-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/UniJIS2004-UTF8-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/UniJIS2004-UTF8-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/UniJISPro-UCS2-HW-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/UniJISPro-UCS2-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/UniJISPro-UTF8-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/UniJISX0213-UTF32-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/UniJISX0213-UTF32-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/UniJISX02132004-UTF32-H
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/UniJISX02132004-UTF32-V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/V
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/CMap/WP-Symbol
%{_texmfdistdir}/fonts/cmap/adobemapping/aj16/cid2code.txt
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/CMap/Adobe-Korea1-0
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/CMap/Adobe-Korea1-1
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/CMap/Adobe-Korea1-2
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/CMap/KSC-EUC-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/CMap/KSC-EUC-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/CMap/KSC-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/CMap/KSC-Johab-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/CMap/KSC-Johab-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/CMap/KSC-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/CMap/KSCms-UHC-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/CMap/KSCms-UHC-HW-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/CMap/KSCms-UHC-HW-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/CMap/KSCms-UHC-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/CMap/KSCpc-EUC-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/CMap/KSCpc-EUC-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/CMap/UniKS-UCS2-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/CMap/UniKS-UCS2-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/CMap/UniKS-UTF16-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/CMap/UniKS-UTF16-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/CMap/UniKS-UTF32-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/CMap/UniKS-UTF32-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/CMap/UniKS-UTF8-H
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/CMap/UniKS-UTF8-V
%{_texmfdistdir}/fonts/cmap/adobemapping/ak12/cid2code.txt
%{_texmfdistdir}/fonts/cmap/adobemapping/cmap-current-versions.txt
%{_texmfdistdir}/fonts/cmap/adobemapping/cmap-readme.txt
%{_texmfdistdir}/fonts/cmap/adobemapping/mapping-readme.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts %{buildroot}%{_texmfdistdir}
