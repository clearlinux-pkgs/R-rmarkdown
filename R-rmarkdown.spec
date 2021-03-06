#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rmarkdown
Version  : 2.9
Release  : 57
URL      : https://cran.r-project.org/src/contrib/rmarkdown_2.9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rmarkdown_2.9.tar.gz
Summary  : Dynamic Documents for R
Group    : Development/Tools
License  : GPL-3.0 MIT
Requires: R-evaluate
Requires: R-htmltools
Requires: R-jsonlite
Requires: R-knitr
Requires: R-stringr
Requires: R-tinytex
Requires: R-xfun
Requires: R-yaml
BuildRequires : R-evaluate
BuildRequires : R-htmltools
BuildRequires : R-jsonlite
BuildRequires : R-knitr
BuildRequires : R-stringr
BuildRequires : R-tinytex
BuildRequires : R-xfun
BuildRequires : R-yaml
BuildRequires : buildreq-R

%description
This a jQuery UI custom build, downloaded from:
http://jqueryui.com/download/#!version=1.11.4&components=1111111111110111111111111111111111111

%prep
%setup -q -c -n rmarkdown
cd %{_builddir}/rmarkdown

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623780352

%install
export SOURCE_DATE_EPOCH=1623780352
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rmarkdown
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rmarkdown
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rmarkdown || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rmarkdown/CITATION
/usr/lib64/R/library/rmarkdown/COPYING
/usr/lib64/R/library/rmarkdown/DESCRIPTION
/usr/lib64/R/library/rmarkdown/INDEX
/usr/lib64/R/library/rmarkdown/Meta/Rd.rds
/usr/lib64/R/library/rmarkdown/Meta/features.rds
/usr/lib64/R/library/rmarkdown/Meta/hsearch.rds
/usr/lib64/R/library/rmarkdown/Meta/links.rds
/usr/lib64/R/library/rmarkdown/Meta/nsInfo.rds
/usr/lib64/R/library/rmarkdown/Meta/package.rds
/usr/lib64/R/library/rmarkdown/Meta/vignette.rds
/usr/lib64/R/library/rmarkdown/NAMESPACE
/usr/lib64/R/library/rmarkdown/NEWS.md
/usr/lib64/R/library/rmarkdown/NOTICE
/usr/lib64/R/library/rmarkdown/R/rmarkdown
/usr/lib64/R/library/rmarkdown/R/rmarkdown.rdb
/usr/lib64/R/library/rmarkdown/R/rmarkdown.rdx
/usr/lib64/R/library/rmarkdown/doc/index.html
/usr/lib64/R/library/rmarkdown/doc/lua-filters.R
/usr/lib64/R/library/rmarkdown/doc/lua-filters.Rmd
/usr/lib64/R/library/rmarkdown/doc/lua-filters.html
/usr/lib64/R/library/rmarkdown/doc/rmarkdown.R
/usr/lib64/R/library/rmarkdown/doc/rmarkdown.Rmd
/usr/lib64/R/library/rmarkdown/doc/rmarkdown.html
/usr/lib64/R/library/rmarkdown/help/AnIndex
/usr/lib64/R/library/rmarkdown/help/aliases.rds
/usr/lib64/R/library/rmarkdown/help/figures/logo.png
/usr/lib64/R/library/rmarkdown/help/paths.rds
/usr/lib64/R/library/rmarkdown/help/rmarkdown.rdb
/usr/lib64/R/library/rmarkdown/help/rmarkdown.rdx
/usr/lib64/R/library/rmarkdown/html/00Index.html
/usr/lib64/R/library/rmarkdown/html/R.css
/usr/lib64/R/library/rmarkdown/rmarkdown/lua/latex-div.lua
/usr/lib64/R/library/rmarkdown/rmarkdown/lua/number-sections.lua
/usr/lib64/R/library/rmarkdown/rmarkdown/lua/pagebreak.lua
/usr/lib64/R/library/rmarkdown/rmarkdown/lua/shared.lua
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
/usr/lib64/R/library/rmarkdown/rmd/h/accessibility/empty-anchor.js
/usr/lib64/R/library/rmarkdown/rmd/h/anchor-sections/anchor-sections.css
/usr/lib64/R/library/rmarkdown/rmd/h/anchor-sections/anchor-sections.js
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/bootstrap-theme.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/bootstrap-theme.css.map
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/bootstrap-theme.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/bootstrap.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/bootstrap.css.map
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/bootstrap.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/cerulean.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/cosmo.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/darkly.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/flatly.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/fonts/Lato.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/fonts/LatoBold.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/fonts/LatoItalic.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/fonts/NewsCycle.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/fonts/NewsCycleBold.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/fonts/OpenSans.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/fonts/OpenSansBold.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/fonts/OpenSansBoldItalic.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/fonts/OpenSansItalic.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/fonts/OpenSansLight.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/fonts/OpenSansLightItalic.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/fonts/Raleway.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/fonts/RalewayBold.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/fonts/Roboto.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/fonts/RobotoBold.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/fonts/RobotoLight.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/fonts/RobotoMedium.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/fonts/SourceSansPro.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/fonts/SourceSansProBold.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/fonts/SourceSansProItalic.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/fonts/SourceSansProLight.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/fonts/Ubuntu.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/journal.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/lumen.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/paper.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/readable.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/sandstone.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/simplex.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/spacelab.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/united.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/css/yeti.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/fonts/glyphicons-halflings-regular.eot
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/fonts/glyphicons-halflings-regular.svg
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/fonts/glyphicons-halflings-regular.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/fonts/glyphicons-halflings-regular.woff
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/fonts/glyphicons-halflings-regular.woff2
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/js/bootstrap.js
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/js/bootstrap.min.js
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/js/npm.js
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/shim/html5shiv.min.js
/usr/lib64/R/library/rmarkdown/rmd/h/bootstrap/shim/respond.min.js
/usr/lib64/R/library/rmarkdown/rmd/h/default.html
/usr/lib64/R/library/rmarkdown/rmd/h/fontawesome/css/all.css
/usr/lib64/R/library/rmarkdown/rmd/h/fontawesome/css/v4-shims.css
/usr/lib64/R/library/rmarkdown/rmd/h/fontawesome/webfonts/fa-brands-400.eot
/usr/lib64/R/library/rmarkdown/rmd/h/fontawesome/webfonts/fa-brands-400.svg
/usr/lib64/R/library/rmarkdown/rmd/h/fontawesome/webfonts/fa-brands-400.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/fontawesome/webfonts/fa-brands-400.woff
/usr/lib64/R/library/rmarkdown/rmd/h/fontawesome/webfonts/fa-brands-400.woff2
/usr/lib64/R/library/rmarkdown/rmd/h/fontawesome/webfonts/fa-regular-400.eot
/usr/lib64/R/library/rmarkdown/rmd/h/fontawesome/webfonts/fa-regular-400.svg
/usr/lib64/R/library/rmarkdown/rmd/h/fontawesome/webfonts/fa-regular-400.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/fontawesome/webfonts/fa-regular-400.woff
/usr/lib64/R/library/rmarkdown/rmd/h/fontawesome/webfonts/fa-regular-400.woff2
/usr/lib64/R/library/rmarkdown/rmd/h/fontawesome/webfonts/fa-solid-900.eot
/usr/lib64/R/library/rmarkdown/rmd/h/fontawesome/webfonts/fa-solid-900.svg
/usr/lib64/R/library/rmarkdown/rmd/h/fontawesome/webfonts/fa-solid-900.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/fontawesome/webfonts/fa-solid-900.woff
/usr/lib64/R/library/rmarkdown/rmd/h/fontawesome/webfonts/fa-solid-900.woff2
/usr/lib64/R/library/rmarkdown/rmd/h/highlightjs/default.css
/usr/lib64/R/library/rmarkdown/rmd/h/highlightjs/highlight.js
/usr/lib64/R/library/rmarkdown/rmd/h/highlightjs/textmate.css
/usr/lib64/R/library/rmarkdown/rmd/h/ionicons/LICENSE
/usr/lib64/R/library/rmarkdown/rmd/h/ionicons/css/ionicons.css
/usr/lib64/R/library/rmarkdown/rmd/h/ionicons/css/ionicons.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/ionicons/fonts/ionicons.ttf
/usr/lib64/R/library/rmarkdown/rmd/h/jquery-AUTHORS.txt
/usr/lib64/R/library/rmarkdown/rmd/h/jquery/jquery.min.js
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui-AUTHORS.txt
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui/README
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui/images/ui-icons_444444_256x240.png
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui/images/ui-icons_555555_256x240.png
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui/images/ui-icons_777620_256x240.png
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui/images/ui-icons_777777_256x240.png
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui/images/ui-icons_cc0000_256x240.png
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui/images/ui-icons_ffffff_256x240.png
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui/index.html
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui/jquery-ui.css
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui/jquery-ui.js
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui/jquery-ui.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui/jquery-ui.min.js
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui/jquery-ui.structure.css
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui/jquery-ui.structure.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui/jquery-ui.theme.css
/usr/lib64/R/library/rmarkdown/rmd/h/jqueryui/jquery-ui.theme.min.css
/usr/lib64/R/library/rmarkdown/rmd/h/navigation-1.1/codefolding.js
/usr/lib64/R/library/rmarkdown/rmd/h/navigation-1.1/sourceembed.js
/usr/lib64/R/library/rmarkdown/rmd/h/navigation-1.1/tabsets.js
/usr/lib64/R/library/rmarkdown/rmd/h/pagedtable-1.1/css/pagedtable.css
/usr/lib64/R/library/rmarkdown/rmd/h/pagedtable-1.1/js/pagedtable.js
/usr/lib64/R/library/rmarkdown/rmd/h/pandoc/header-attrs.js
/usr/lib64/R/library/rmarkdown/rmd/h/rmarkdown/rmd_loader.css
/usr/lib64/R/library/rmarkdown/rmd/h/rmarkdown/rmd_loader.gif
/usr/lib64/R/library/rmarkdown/rmd/h/rmarkdown/rmd_loader.js
/usr/lib64/R/library/rmarkdown/rmd/h/rmarkdown/rmd_perf.css
/usr/lib64/R/library/rmarkdown/rmd/h/rmarkdown/rmd_perf.js
/usr/lib64/R/library/rmarkdown/rmd/h/rsiframe-1.1/rsiframe.js
/usr/lib64/R/library/rmarkdown/rmd/h/tocify/jquery.tocify.css
/usr/lib64/R/library/rmarkdown/rmd/h/tocify/jquery.tocify.js
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
/usr/lib64/R/library/rmarkdown/rmd/latex/subtitle.tex
/usr/lib64/R/library/rmarkdown/rmd/site/_site.yml
/usr/lib64/R/library/rmarkdown/rmd/site/about.Rmd
/usr/lib64/R/library/rmarkdown/rmd/site/index.Rmd
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
/usr/lib64/R/library/rmarkdown/rmd/slidy/slidy_shiny.js
/usr/lib64/R/library/rmarkdown/rstudio/templates/project/skeleton.dcf
/usr/lib64/R/library/rmarkdown/tests/rmd/output_dir.Rmd
/usr/lib64/R/library/rmarkdown/tests/rmd/raw-header.Rmd
/usr/lib64/R/library/rmarkdown/tests/rmd/two-authors.Rmd
/usr/lib64/R/library/rmarkdown/tests/rmd/two-bibs.Rmd
/usr/lib64/R/library/rmarkdown/tests/rmd/word.Rmd
/usr/lib64/R/library/rmarkdown/tests/rmd/yaml-r-code.Rmd
/usr/lib64/R/library/rmarkdown/tests/shiny/01-basic-input.Rmd
/usr/lib64/R/library/rmarkdown/tests/shiny/02-data-table.Rmd
/usr/lib64/R/library/rmarkdown/tests/shiny/03-rm-all.Rmd
/usr/lib64/R/library/rmarkdown/tests/shiny/04-prerendered-envir.Rmd
/usr/lib64/R/library/rmarkdown/tests/testrmd.R
/usr/lib64/R/library/rmarkdown/tests/testthat.R
/usr/lib64/R/library/rmarkdown/tests/testthat/_snaps/github_document/github-atx.md
/usr/lib64/R/library/rmarkdown/tests/testthat/_snaps/github_document/github-toc.md
/usr/lib64/R/library/rmarkdown/tests/testthat/_snaps/html_dependencies.md
/usr/lib64/R/library/rmarkdown/tests/testthat/_snaps/lua-filters.md
/usr/lib64/R/library/rmarkdown/tests/testthat/_snaps/render/A.split.md
/usr/lib64/R/library/rmarkdown/tests/testthat/_snaps/render/B.split.md
/usr/lib64/R/library/rmarkdown/tests/testthat/helpers.R
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/csvs/csv1.csv
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/csvs/csv2.csv
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/csvs/other/csv3.csv
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/dep1.html
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/dep2.html
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/directory-refs.Rmd
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/empty.Rmd
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/empty.bib
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/empty.csl
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/empty.css
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/empty.csv
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/empty.html
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/empty.jpg
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/empty.js
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/empty.md
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/empty.png
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/empty.tsv
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/empty/empty.csv
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/file-exists.Rmd
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/has-css.Rmd
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/has-image.css
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/html.html
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/markdown.md
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/multi-includes.Rmd
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/nonempty/empty.csv
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/nonempty/empty.jpg
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/pdf.Rmd
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/period.Rmd
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/quotes.Rmd
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/r-notebook.Rmd
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/readcsv-source.R
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/readcsv.R
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/readcsv.Rmd
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/resource-files.Rmd
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/rmarkdown.Rmd
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/styles.css
/usr/lib64/R/library/rmarkdown/tests/testthat/resources/tinyplot.png
/usr/lib64/R/library/rmarkdown/tests/testthat/site/PageA.Rmd
/usr/lib64/R/library/rmarkdown/tests/testthat/site/PageB.rmd
/usr/lib64/R/library/rmarkdown/tests/testthat/site/PageC.md
/usr/lib64/R/library/rmarkdown/tests/testthat/site/PageD.R
/usr/lib64/R/library/rmarkdown/tests/testthat/site/_site.yml
/usr/lib64/R/library/rmarkdown/tests/testthat/site/docs.txt
/usr/lib64/R/library/rmarkdown/tests/testthat/site/index.Rmd
/usr/lib64/R/library/rmarkdown/tests/testthat/site/script.R
/usr/lib64/R/library/rmarkdown/tests/testthat/site/styles.css
/usr/lib64/R/library/rmarkdown/tests/testthat/test-encode-decode.R
/usr/lib64/R/library/rmarkdown/tests/testthat/test-formats.R
/usr/lib64/R/library/rmarkdown/tests/testthat/test-formats.Rmd
/usr/lib64/R/library/rmarkdown/tests/testthat/test-github_document.R
/usr/lib64/R/library/rmarkdown/tests/testthat/test-html_dependencies.R
/usr/lib64/R/library/rmarkdown/tests/testthat/test-htmlparse.R
/usr/lib64/R/library/rmarkdown/tests/testthat/test-ioslides.R
/usr/lib64/R/library/rmarkdown/tests/testthat/test-knit_print.R
/usr/lib64/R/library/rmarkdown/tests/testthat/test-lua-filters.R
/usr/lib64/R/library/rmarkdown/tests/testthat/test-notebook.R
/usr/lib64/R/library/rmarkdown/tests/testthat/test-output_format.R
/usr/lib64/R/library/rmarkdown/tests/testthat/test-params.R
/usr/lib64/R/library/rmarkdown/tests/testthat/test-render.R
/usr/lib64/R/library/rmarkdown/tests/testthat/test-resources.R
/usr/lib64/R/library/rmarkdown/tests/testthat/test-shiny.R
/usr/lib64/R/library/rmarkdown/tests/testthat/test-shiny_prerendered.R
/usr/lib64/R/library/rmarkdown/tests/testthat/test-site.R
/usr/lib64/R/library/rmarkdown/tests/testthat/test-spin.R
/usr/lib64/R/library/rmarkdown/tests/testthat/test-utils.R
/usr/lib64/R/library/rmarkdown/tests/testthat/test-vignette.R
/usr/lib64/R/library/rmarkdown/tests/testthat/test-yml-parsing.R
