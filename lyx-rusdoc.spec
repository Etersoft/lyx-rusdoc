Name: lyx-rusdoc
Version: 1.2
Release: alt2

Packager: Vitaly Lipatov <lav@altlinux.ru>

Summary: The documentation for LyX and GOST text class
Summary(ru_RU.KOI8-R): Русская документация по LyX и классу текста GOST
License: GPL
Url: http://rulyx.narod.ru
Group: Office
Source: %name-%version.tar.bz2
BuildArchitectures: noarch

Requires: lyx >= 1.2.0

%description
The %name package contains additional describes in russian
for LyX, and the documentation for LyX/LaTeX class GOST.

%description -l ru_RU.KOI8-R
Пакет %name содержит дополнительные описания LyX'а
на русском языке, а также документацию для класса текста GOST LyX/LaTeX,
предназначенного для подготовки технической текстовой документации
в соответствии с ГОСТ 2.105-95.

%prep
%setup -q

%install
cd doc
for i in *
do
	install -D -m644 $i $RPM_BUILD_ROOT/%_datadir/doc/%name-%version/$i
done
cd -
cd GOST-LyX
for i in *
do
	install -D -m644 $i $RPM_BUILD_ROOT/%_datadir/doc/%name-%version/GOST-LyX/$i
done
cd -
cd lyx-ug
for i in *
do
	install -D -m644 $i $RPM_BUILD_ROOT/%_datadir/doc/%name-%version/LyX-UG/$i
done
cd -

%post
%preun
%postun
%files
%docdir %_datadir/doc/%name-%version
%_datadir/doc/%name-%version

%changelog
* Thu Nov 14 2002 Stanislav Ievlev <inger@altlinux.ru> 1.2-alt2
- rebuild

* Fri Jun 14 2002 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- update all files for LyX 1.2.0
- add noarch option

* Sun Apr 14 2002 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- update GOST-LyX
- add lyx-ug (introduction in LyX for newbie)

* Tue Dec 24 2001 23:01:01 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- first version
