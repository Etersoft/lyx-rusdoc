#!/bin/sh
# 11.12.01 (c) Vitaly Lipatov <vitlav@mail.ru>
# 30.08.02, 19.10.03 (c) Vitaly Lipatov <lav@altlinux.ru>

# Use: pdf2booklet namefile.pdf (at A4 format)
# На основании входного PDF A4-формата формируем два файла,
# для распечатки каждого файла на своей стороне бумаги.

BASE=`basename "$1" .pdf`
INFILE=$BASE.ps
pdftops -paper A4 "$1" $INFILE
#pdf2ps "$1" $INFILE

OUTFILE=$BASE.out.ps
OUTFILE1=$BASE.out1.ps
OUTFILE2=$BASE.out2.ps

#cat "$INFILE" |pstops -pa4 "(-1cm,0)" | psbook | psnup -2 -Pa4 -pa4 | pstops "(0,-1.5cm)" > $OUTFILE
cat "$INFILE" |pstops -pa4 "(-1cm,0)" | psbook | psnup -2 -Pa4 -pa4 | pstops "(0,-1cm)" > $OUTFILE
psselect -o <$OUTFILE >$OUTFILE1
psselect -e -r <$OUTFILE >$OUTFILE2

gv -seascape -scale 1 $OUTFILE1
gv -seascape -scale 1 $OUTFILE2
rm -f $OUTFILE
rm -f $INFILE
