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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package comprises the collection of CMap and PDF mapping files made
available for distribution by Adobe.

%prep
%setup -q -c
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
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/fonts/cmap
%dir %{_datadir}/texmf-dist/fonts/cmap/adobemapping
%dir %{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources
%dir %{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf
%dir %{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7
%dir %{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5
%dir %{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Identity-0
%dir %{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7
%dir %{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-KR-9
%dir %{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2
%dir %{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other
%dir %{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2unicode
%dir %{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap
%dir %{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap
%dir %{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Identity-0/CMap
%dir %{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap
%dir %{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-KR-9/CMap
%dir %{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/README
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/Adobe-CNS1-0
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/Adobe-CNS1-1
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/Adobe-CNS1-2
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/Adobe-CNS1-3
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/Adobe-CNS1-4
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/Adobe-CNS1-5
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/Adobe-CNS1-6
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/Adobe-CNS1-7
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/B5-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/B5-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/B5pc-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/B5pc-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/CNS-EUC-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/CNS-EUC-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/CNS1-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/CNS1-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/CNS2-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/CNS2-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/ETHK-B5-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/ETHK-B5-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/ETen-B5-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/ETen-B5-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/ETenms-B5-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/ETenms-B5-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/HKdla-B5-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/HKdla-B5-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/HKdlb-B5-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/HKdlb-B5-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/HKgccs-B5-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/HKgccs-B5-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/HKm314-B5-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/HKm314-B5-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/HKm471-B5-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/HKm471-B5-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/HKscs-B5-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/HKscs-B5-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/UniCNS-UCS2-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/UniCNS-UCS2-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/UniCNS-UTF16-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/UniCNS-UTF16-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/UniCNS-UTF32-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/UniCNS-UTF32-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/UniCNS-UTF8-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/CMap/UniCNS-UTF8-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-CNS1-7/cid2code.txt
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/Adobe-GB1-0
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/Adobe-GB1-1
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/Adobe-GB1-2
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/Adobe-GB1-3
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/Adobe-GB1-4
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/Adobe-GB1-5
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/GB-EUC-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/GB-EUC-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/GB-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/GB-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/GBK-EUC-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/GBK-EUC-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/GBK2K-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/GBK2K-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/GBKp-EUC-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/GBKp-EUC-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/GBT-EUC-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/GBT-EUC-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/GBT-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/GBT-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/GBTpc-EUC-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/GBTpc-EUC-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/GBpc-EUC-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/GBpc-EUC-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/UniGB-UCS2-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/UniGB-UCS2-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/UniGB-UTF16-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/UniGB-UTF16-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/UniGB-UTF32-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/UniGB-UTF32-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/UniGB-UTF8-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/CMap/UniGB-UTF8-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-GB1-5/cid2code.txt
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Identity-0/CMap/Identity-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Identity-0/CMap/Identity-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/78-EUC-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/78-EUC-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/78-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/78-RKSJ-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/78-RKSJ-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/78-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/78ms-RKSJ-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/78ms-RKSJ-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/83pv-RKSJ-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/90ms-RKSJ-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/90ms-RKSJ-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/90msp-RKSJ-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/90msp-RKSJ-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/90pv-RKSJ-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/90pv-RKSJ-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/Add-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/Add-RKSJ-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/Add-RKSJ-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/Add-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/Adobe-Japan1-0
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/Adobe-Japan1-1
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/Adobe-Japan1-2
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/Adobe-Japan1-3
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/Adobe-Japan1-4
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/Adobe-Japan1-5
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/Adobe-Japan1-6
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/Adobe-Japan1-7
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/EUC-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/EUC-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/Ext-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/Ext-RKSJ-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/Ext-RKSJ-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/Ext-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/Hankaku
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/Hiragana
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/Katakana
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/NWP-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/NWP-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/RKSJ-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/RKSJ-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/Roman
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/UniJIS-UCS2-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/UniJIS-UCS2-HW-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/UniJIS-UCS2-HW-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/UniJIS-UCS2-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/UniJIS-UTF16-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/UniJIS-UTF16-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/UniJIS-UTF32-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/UniJIS-UTF32-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/UniJIS-UTF8-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/UniJIS-UTF8-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/UniJIS2004-UTF16-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/UniJIS2004-UTF16-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/UniJIS2004-UTF32-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/UniJIS2004-UTF32-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/UniJIS2004-UTF8-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/UniJIS2004-UTF8-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/UniJISPro-UCS2-HW-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/UniJISPro-UCS2-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/UniJISPro-UTF8-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/UniJISX0213-UTF32-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/UniJISX0213-UTF32-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/UniJISX02132004-UTF32-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/UniJISX02132004-UTF32-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/CMap/WP-Symbol
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/cid2code.txt
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/jisx0208-jp04.txt
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/jisx0208-jp90.txt
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/jisx0212-jp04.txt
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/jisx0212-jp90.txt
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/jisx0213-jp04.txt
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Japan1-7/jisx0213-jp90.txt
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-KR-9/CMap/Adobe-KR-0
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-KR-9/CMap/Adobe-KR-1
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-KR-9/CMap/Adobe-KR-2
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-KR-9/CMap/Adobe-KR-3
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-KR-9/CMap/Adobe-KR-4
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-KR-9/CMap/Adobe-KR-5
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-KR-9/CMap/Adobe-KR-6
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-KR-9/CMap/Adobe-KR-7
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-KR-9/CMap/Adobe-KR-8
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-KR-9/CMap/Adobe-KR-9
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-KR-9/CMap/UniAKR-UTF16-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-KR-9/CMap/UniAKR-UTF32-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-KR-9/CMap/UniAKR-UTF8-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-KR-9/cid2code.txt
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap/Adobe-Korea1-0
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap/Adobe-Korea1-1
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap/Adobe-Korea1-2
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap/KSC-EUC-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap/KSC-EUC-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap/KSC-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap/KSC-Johab-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap/KSC-Johab-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap/KSC-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap/KSCms-UHC-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap/KSCms-UHC-HW-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap/KSCms-UHC-HW-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap/KSCms-UHC-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap/KSCpc-EUC-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap/KSCpc-EUC-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap/UniKS-UCS2-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap/UniKS-UCS2-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap/UniKS-UTF16-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap/UniKS-UTF16-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap/UniKS-UTF32-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap/UniKS-UTF32-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap/UniKS-UTF8-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/CMap/UniKS-UTF8-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Adobe-Korea1-2/cid2code.txt
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/LICENSE.md
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/Makefile
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/README.md
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/cmap-resources/VERSIONS.txt
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/LICENSE.txt
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/Makefile
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/README.md
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/90ms-RKSJ-UCS2
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/90pv-RKSJ-UCS2
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/90pv-RKSJ-UCS2C
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/Adobe-CNS1-B5pc
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/Adobe-CNS1-ETen-B5
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/Adobe-CNS1-H-CID
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/Adobe-CNS1-H-Host
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/Adobe-CNS1-H-Mac
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/Adobe-GB1-GBK-EUC
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/Adobe-GB1-GBpc-EUC
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/Adobe-GB1-H-CID
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/Adobe-GB1-H-Host
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/Adobe-GB1-H-Mac
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/Adobe-Japan1-90ms-RKSJ
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/Adobe-Japan1-90pv-RKSJ
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/Adobe-Japan1-H-CID
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/Adobe-Japan1-H-Host
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/Adobe-Japan1-H-Mac
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/Adobe-Japan1-PS-H
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/Adobe-Japan1-PS-V
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/Adobe-Korea1-H-CID
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/Adobe-Korea1-H-Host
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/Adobe-Korea1-H-Mac
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/Adobe-Korea1-KSCms-UHC
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/Adobe-Korea1-KSCpc-EUC
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/B5pc-UCS2
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/B5pc-UCS2C
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/ETen-B5-UCS2
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/GBK-EUC-UCS2
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/GBpc-EUC-UCS2
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/GBpc-EUC-UCS2C
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/KSCms-UHC-UCS2
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/KSCpc-EUC-UCS2
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/KSCpc-EUC-UCS2C
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/UCS2-90ms-RKSJ
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/UCS2-90pv-RKSJ
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/UCS2-B5pc
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/UCS2-ETen-B5
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/UCS2-GBK-EUC
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/UCS2-GBpc-EUC
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/UCS2-KSCms-UHC
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2other/UCS2-KSCpc-EUC
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2unicode/Adobe-CNS1-UCS2
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2unicode/Adobe-GB1-UCS2
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2unicode/Adobe-Japan1-UCS2
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2unicode/Adobe-KR-UCS2
%{_datadir}/texmf-dist/fonts/cmap/adobemapping/mapping-resources-pdf/pdf2unicode/Adobe-Korea1-UCS2
