#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ordinalCont
Version  : 2.0.2
Release  : 10
URL      : https://cran.r-project.org/src/contrib/ordinalCont_2.0.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ordinalCont_2.0.2.tar.gz
Summary  : Ordinal Regression Analysis for Continuous Scales
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-Deriv
BuildRequires : R-Deriv
BuildRequires : buildreq-R

%description
self-rating scales such as the Visual Analog Scale (VAS) used in pain
    assessment, or the Linear Analog Self-Assessment (LASA) scales in quality
    of life studies. These scales measure subjects' perception of an intangible
    quantity, and cannot be handled as ratio variables because of their inherent
    non-linearity. We treat them as ordinal variables, measured on a continuous
    scale. A function (the g function) connects the scale with an underlying
    continuous latent variable. The link function is the inverse of the CDF of the
    assumed underlying distribution of the latent variable. A variety of

%prep
%setup -q -c -n ordinalCont
cd %{_builddir}/ordinalCont

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649174577

%install
export SOURCE_DATE_EPOCH=1649174577
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ordinalCont
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ordinalCont
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ordinalCont
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc ordinalCont || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ordinalCont/CITATION
/usr/lib64/R/library/ordinalCont/DESCRIPTION
/usr/lib64/R/library/ordinalCont/INDEX
/usr/lib64/R/library/ordinalCont/Meta/Rd.rds
/usr/lib64/R/library/ordinalCont/Meta/data.rds
/usr/lib64/R/library/ordinalCont/Meta/features.rds
/usr/lib64/R/library/ordinalCont/Meta/hsearch.rds
/usr/lib64/R/library/ordinalCont/Meta/links.rds
/usr/lib64/R/library/ordinalCont/Meta/nsInfo.rds
/usr/lib64/R/library/ordinalCont/Meta/package.rds
/usr/lib64/R/library/ordinalCont/NAMESPACE
/usr/lib64/R/library/ordinalCont/NEWS
/usr/lib64/R/library/ordinalCont/R/ordinalCont
/usr/lib64/R/library/ordinalCont/R/ordinalCont.rdb
/usr/lib64/R/library/ordinalCont/R/ordinalCont.rdx
/usr/lib64/R/library/ordinalCont/data/Rdata.rdb
/usr/lib64/R/library/ordinalCont/data/Rdata.rds
/usr/lib64/R/library/ordinalCont/data/Rdata.rdx
/usr/lib64/R/library/ordinalCont/help/AnIndex
/usr/lib64/R/library/ordinalCont/help/aliases.rds
/usr/lib64/R/library/ordinalCont/help/ordinalCont.rdb
/usr/lib64/R/library/ordinalCont/help/ordinalCont.rdx
/usr/lib64/R/library/ordinalCont/help/paths.rds
/usr/lib64/R/library/ordinalCont/html/00Index.html
/usr/lib64/R/library/ordinalCont/html/R.css
