Name: lyx-rusdoc
Version: 1.3.4
Release: alt1

Summary: The documentation for LyX and GOST text class
Summary(ru_RU.KOI8-R): Русская документация по LyX и классу текста GOST
License: GPL
Group: Office
URL: http://www.etersoft.ru

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar.bz2

BuildArchitectures: noarch
Requires: lyx-gost

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
for i in *.lyx
do
	install -D -m644 $i ${RPM_BUILD_ROOT}/%_datadir/doc/%name-%version/$i
done
for i in *.sh
do
	install -D -m755 $i ${RPM_BUILD_ROOT}/%_bindir/`basename $i .sh`
done
cd -

cp -rp GOST-LyX/* ${RPM_BUILD_ROOT}/%_datadir/doc/%name-%version/

cd lyx-ug
for i in *
do
	install -D -m644 $i ${RPM_BUILD_ROOT}/%_datadir/doc/%name-%version/LyX-UG/$i
done
cd -

%files
%docdir %_datadir/doc/%name-%version
%_datadir/doc/%name-%version
%_bindir/*

%changelog
* Fri Jun 18 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt1
- update LyX-GOST for last LyX features
- rename scripts and set execute permission on it

* Mon Jan 05 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- update all files for LyX 1.3.3
- spec cleanup
- add scripts for PS-booklets printing

* Fri Jun 14 2002 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- update all files for LyX 1.2.0
- add noarch option

* Sun Apr 14 2002 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- update GOST-LyX
- add lyx-ug (introduction in LyX for newbie)

* Tue Dec 24 2001 23:01:01 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- first version
