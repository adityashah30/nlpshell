#!/bin/bash
base_dir=$PWD
source_dir=$PWD/source
mkdir ManPageCrawler
cd ManPageCrawler
cp $source_dir/getmanpages.sh .
chmod a+x getmanpages.sh
mkdir manpages
mkdir packagelists
mkdir Spider
mkdir programs
cd manpages
declare -a alphabets=("a" "b" "c" "d" "e" "f" "g" "h" "i" "j" "k" "l" "m" "n" "o" "p" "q" "r" "s" "t" "u" "v" "w" "x" "y" "z" "other")
for alphabet in ${alphabets[@]};
do
	mkdir $alphabet
done
cd ..
cd packagelists
for alphabet in ${alphabets[@]};
do
	touch $alphabet"packages.json"
done
cd ..
cd Spider
cp -r $source_dir/Spider/* .
cd ..
cd programs
cp $source_dir/programs/* .