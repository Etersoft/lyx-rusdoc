#!/bin/sh
# 11.12.01 (c) Vitaly Lipatov <vitlav@mail.ru>
# Use: ps2booklet namefile.ps (at A5 format)
# На основании входного постскрипта A5 формата формируем два файла,
# для распечатки каждого файла на своей стороне бумаги.
OUTFILE=`basename "$1" .ps`.out.ps
OUTFILE1=`basename "$1" .ps`.out1.ps
OUTFILE2=`basename "$1" .ps`.out2.ps
cat "$1" | psbook | psnup -2 -Pa5 -pa4  > $OUTFILE
psselect -o <$OUTFILE >$OUTFILE1
psselect -e -r <$OUTFILE >$OUTFILE2
