#!/bin/sh
# 11.12.01, 04.12.02 (c) Vitaly Lipatov <lav@altlinux.ru>
# Use: ps2booklet namefile.ps (at A5 format)
# На основании входного постскрипта A5 формата формируем два файла,
# для распечатки каждого файла на своей стороне бумаги.
BASENAME=`basename "$1" .ps`
OUTFILE=$BASENAME.out.ps
OUTFILE1=$BASENAME.out1.ps
OUTFILE2=$BASENAME.out2.ps
cat "$1" | psbook | psnup -2 -Pa5 -pa4  > $OUTFILE
psselect -o <$OUTFILE >$OUTFILE1
psselect -e -r <$OUTFILE >$OUTFILE2
