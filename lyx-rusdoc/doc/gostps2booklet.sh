#!/bin/sh
# 20.02.03 (c) Vitaly Lipatov <lav@altlinux.ru>
# Выводит каждую страницу уменьшенной, в рамке
# В качестве параметра указывается PostScipt-файл формата A4

OUTFILE=`basename "$1" .ps`.out.ps
OUTFILE1=`basename "$1" .ps`.out1.ps
OUTFILE2=`basename "$1" .ps`.out2.ps
cat "$1" | psbook | psresize -w20cm -h30cm -PA4 | psnup -2 -m0.3cm > $OUTFILE
psselect -o <$OUTFILE >$OUTFILE1
psselect -e -r <$OUTFILE >$OUTFILE2
