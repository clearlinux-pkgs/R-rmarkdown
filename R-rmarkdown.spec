#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rmarkdown
Version  : 1.10
Release  : 14
URL      : https://cran.r-project.org/src/contrib/rmarkdown_1.10.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rmarkdown_1.10.tar.gz
Summary  : Dynamic Documents for R
Group    : Development/Tools
License  : GPL-3.0 MIT
Requires: R-base64enc
Requires: R-htmltools
Requires: R-jsonlite
Requires: R-mime
Requires: R-rprojroot
Requires: R-shiny
Requires: R-stringi
Requires: R-tinytex
BuildRequires : R-base64enc
BuildRequires : R-htmltools
BuildRequires : R-jsonlite
BuildRequires : R-mime
BuildRequires : R-rprojroot
BuildRequires : R-shiny
BuildRequires : R-stringi
BuildRequires : R-tinytex
BuildRequires : clr-R-helpers

%description
This a jQuery UI custom build, downloaded from:
http://jqueryui.com/download/#!version=1.11.4&components=1111111111110111111111111111111111111

%prep
%setup -q -c -n rmarkdown

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529070239

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1529070239
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rmarkdown
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rmarkdown
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rmarkdown
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library rmarkdown|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rmarkdown/COPYING
/usr/lib64/R/library/rmarkdown/DESCRIPTION
/usr/lib64/R/library/rmarkdown/INDEX
/usr/lib64/R/library/rmarkdown/Meta/Rd.rds
/usr/lib64/R/library/rmarkdown/Meta/features.rds
/usr/lib64/R/library/rmarkdown/Meta/hsearch.rds
/usr/lib64/R/library/rmarkdown/Meta/links.rds
/usr/lib64/R/library/rmarkdown/Meta/nsInfo.rds
/usr/lib64/R/library/rmarkdown/Meta/package.rds
/usr/lib64/R/library/rmarkdown/NAMESPACE
/usr/lib64/R/library/rmarkdown/NEWS
/usr/lib64/R/library/rmarkdown/NOTICE
/usr/lib64/R/library/rmarkdown/R/rmarkdown
/usr/lib64/R/library/rmarkdown/R/rmarkdown.rdb
/usr/lib64/R/library/rmarkdown/R/rmarkdown.rdx
/usr/lib64/R/library/rmarkdown/help/AnIndex
/usr/lib64/R/library/rmarkdown/help/aliases.rds
/usr/lib64/R/library/rmarkdown/help/paths.rds
/usr/lib64/R/library/rmarkdown/help/rmarkdown.rdb
/usr/lib64/R/library/rmarkdown/help/rmarkdown.rdx
/usr/lib64/R/library/rmarkdown/html/00Index.html
/usr/lib64/R/library/rmarkdown/html/R.css
/usr/lib64/R/library/rmarkdown/rmarkdown/templates/github_document/resources/default.md
/usr/lib64/R/library/rmarkdown/rmarkdown/templates/github_document/resources/github.css
/usr/lib64/R/library/rmarkdown/rmarkdown/templates/github_document/resources/preview.html
/usr/lib64/R/library/rmarkdown/rmarkdown/templates/github_document/skeleton/skeleton.Rmd
/usr/lib64/R/library/rmarkdown/rmarkdown/templates/github_document/template.yaml
/usr/lib64/R/library/rmarkdown/rmarkdown/templates/html_vignette/resources/vignette.css
/usr/lib64/R/library/rmarkdown/rmarkdown/templates/html_vignette/skeleton/skeleton.Rmd
/usr/lib64/R/library/rmarkdown/rmarkdown/templates/html_vignette/template.yaml
/usr/lib64/R/library/rmarkdown/rmd/fragment/default.html
/usr/lib64/R/library/rmarkdown/rmd/fragment/default.tex
/usr/lib64/R/library/rmarkdown/rmd/h/_navbar.html
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/bootstrap-theme.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/bootstrap-theme.css.map
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/bootstrap-theme.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/bootstrap.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/bootstrap.css.map
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/bootstrap.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/cerulean.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/cosmo.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/flatly.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/fonts/Lato.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/fonts/LatoBold.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/fonts/LatoItalic.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/fonts/NewsCycle.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/fonts/NewsCycleBold.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/fonts/OpenSans.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/fonts/OpenSansBold.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/fonts/OpenSansBoldItalic.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/fonts/OpenSansItalic.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/fonts/OpenSansLight.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/fonts/OpenSansLightItalic.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/fonts/Raleway.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/fonts/RalewayBold.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/fonts/Roboto.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/fonts/RobotoBold.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/fonts/RobotoLight.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/fonts/RobotoMedium.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/fonts/SourceSansPro.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/fonts/SourceSansProBold.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/fonts/SourceSansProItalic.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/fonts/SourceSansProLight.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/fonts/Ubuntu.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/journal.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/lumen.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/paper.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/readable.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/sandstone.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/simplex.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/spacelab.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/united.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/css/yeti.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/fonts/glyphicons-halflings-regular.eot
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/fonts/glyphicons-halflings-regular.svg
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/fonts/glyphicons-halflings-regular.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/fonts/glyphicons-halflings-regular.woff
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/fonts/glyphicons-halflings-regular.woff2
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/js/bootstrap.js
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/js/bootstrap.min.js
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/js/npm.js
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/shim/html5shiv.min.js
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap-3.3.5/shim/respond.min.js
/usr/lib64/R/library/rmarkdown/rmd/h/default.html
/usr/lib64/R/library/rmarkdown/rmd/h/fontawesome/css/fa-svg-with-js.css
/usr/lib64/R/library/rmarkdown/rmd/h/fontawesome/fonts/fa-brands-400.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/fontawesome/fonts/fa-regular-400.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/fontawesome/fonts/fa-solid-900.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/fontawesome/js/fa-v4-shims.min.js
/usr/lib64/R/library/rmarkdown/rmd/h/fontawesome/js/fontawesome-all.min.js
/usr/lib64/R/library/rmarkdown/rmd/h/highlightjs/default.css
/usr/lib64/R/library/rmarkdown/rmd/h/highlightjs/highlight.js
/usr/lib64/R/library/rmarkdown/rmd/h/highlightjs/textmate.css
/usr/lib64/R/library/rmarkdown/rmd/h/ionicons-2.0.1/LICENSE
/usr/lib64/R/library/rmarkdown/rmd/h/ionicons-2.0.1/css/ionicons.css
/usr/lib64/R/library/rmarkdown/rmd/h/ionicons-2.0.1/css/ionicons.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/ionicons-2.0.1/fonts/ionicons.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/jquery-1.11.3/jquery.min.js
/usr/lib64/R/library/rmarkdown/rmd/h/jquery-AUTHORS.txt
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui-1.11.4/README
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui-1.11.4/images/ui-icons_444444_256x240.png
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui-1.11.4/images/ui-icons_555555_256x240.png
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui-1.11.4/images/ui-icons_777620_256x240.png
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui-1.11.4/images/ui-icons_777777_256x240.png
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui-1.11.4/images/ui-icons_cc0000_256x240.png
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui-1.11.4/images/ui-icons_ffffff_256x240.png
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui-1.11.4/index.html
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui-1.11.4/jquery-ui.css
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui-1.11.4/jquery-ui.js
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui-1.11.4/jquery-ui.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui-1.11.4/jquery-ui.min.js
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui-1.11.4/jquery-ui.structure.css
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui-1.11.4/jquery-ui.structure.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui-1.11.4/jquery-ui.theme.css
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui-1.11.4/jquery-ui.theme.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui-AUTHORS.txt
/usr/lib64/R/library/rmarkdown/rmd/h/navigation-1.1/codefolding.js
/usr/lib64/R/library/rmarkdown/rmd/h/navigation-1.1/sourceembed.js
/usr/lib64/R/library/rmarkdown/rmd/h/navigation-1.1/tabsets.js
/usr/lib64/R/library/rmarkdown/rmd/h/pagedtable-1.1/css/pagedtable.css
/usr/lib64/R/library/rmarkdown/rmd/h/pagedtable-1.1/js/pagedtable.js
/usr/lib64/R/library/rmarkdown/rmd/h/rmarkdown/rmd_loader.css
/usr/lib64/R/library/rmarkdown/rmd/h/rmarkdown/rmd_loader.gif
/usr/lib64/R/library/rmarkdown/rmd/h/rmarkdown/rmd_loader.js
/usr/lib64/R/library/rmarkdown/rmd/h/rmarkdown/rmd_perf.css
/usr/lib64/R/library/rmarkdown/rmd/h/rmarkdown/rmd_perf.js
/usr/lib64/R/library/rmarkdown/rmd/h/rsiframe-1.1/rsiframe.js
/usr/lib64/R/library/rmarkdown/rmd/h/tocify-1.9.1/jquery.tocify.css
/usr/lib64/R/library/rmarkdown/rmd/h/tocify-1.9.1/jquery.tocify.js
/usr/lib64/R/library/rmarkdown/rmd/ioslides/default.html
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides-13.5.1/fonts/OpenSans.ttf
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides-13.5.1/fonts/OpenSansItalic.ttf
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides-13.5.1/fonts/OpenSansSemibold.ttf
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides-13.5.1/fonts/OpenSansSemiboldItalic.ttf
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides-13.5.1/fonts/SourceCodePro.ttf
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides-13.5.1/fonts/fonts.css
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides-13.5.1/images/google_developers_icon_128.png
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides-13.5.1/js/hammer.js
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides-13.5.1/js/modernizr.custom.45394.js
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides-13.5.1/js/order.js
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides-13.5.1/js/polyfills/classList.min.js
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides-13.5.1/js/polyfills/dataset.min.js
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides-13.5.1/js/polyfills/history.min.js
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides-13.5.1/js/prettify/lang-r.js
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides-13.5.1/js/prettify/lang-tex.js
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides-13.5.1/js/prettify/lang-yaml.js
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides-13.5.1/js/prettify/prettify.css
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides-13.5.1/js/prettify/prettify.js
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides-13.5.1/js/require-1.0.8.min.js
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides-13.5.1/js/slide-controller.js
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides-13.5.1/js/slide-deck.js
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides-13.5.1/theme/css/default.css
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides-13.5.1/theme/css/phone.css
/usr/lib64/R/library/rmarkdown/rmd/ioslides/ioslides_presentation.lua
/usr/lib64/R/library/rmarkdown/rmd/latex/default-1.14.tex
/usr/lib64/R/library/rmarkdown/rmd/latex/default-1.15.2.tex
/usr/lib64/R/library/rmarkdown/rmd/latex/default-1.17.0.2.tex
/usr/lib64/R/library/rmarkdown/rmd/latex/default.tex
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/bullet-fold-dim.gif
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/bullet-fold-dim.png
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/bullet-fold.gif
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/bullet-fold.png
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/bullet-nofold-dim.gif
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/bullet-nofold-dim.png
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/bullet-nofold.gif
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/bullet-nofold.png
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/bullet-unfold-dim.gif
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/bullet-unfold-dim.png
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/bullet-unfold.gif
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/bullet-unfold.png
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/bullet.gif
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/bullet.png
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/example.png
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/example.svg
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/face1.gif
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/face2.gif
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/face3.gif
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/face4.gif
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/fold-bright.gif
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/fold-dim.bmp
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/fold-dim.gif
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/fold.bmp
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/fold.gif
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/icon-blue.png
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/keys2.jpg
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/nofold-dim.bmp
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/nofold-dim.gif
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/nofold.bmp
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/unfold-bright.gif
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/unfold-dim.bmp
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/unfold-dim.gif
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/unfold.bmp
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/unfold.gif
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/w3c-logo-blue.gif
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/w3c-logo-blue.svg
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/w3c-logo-slanted.jpg
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/w3c-logo-white.gif
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/graphics/w3c-logo-white.svg
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/scripts/img.srcset.js
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/scripts/slidy-irc.js
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/scripts/slidy.js
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/scripts/slidy.js.gz
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/styles/slidy.css
/usr/lib64/R/library/rmarkdown/rmd/slidy/Slidy2/styles/w3c-blue.css
/usr/lib64/R/library/rmarkdown/rmd/slidy/default.html
