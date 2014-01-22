#/bin/bash
base_dir=$PWD
cd Spider
base_url="http://linux.die.net/man/"
extension=".html"
declare -a alphabets=("a" "b" "c" "d" "e" "f" "g" "h" "i" "j" "k" "l" "m" "n" "o" "p" "q" "r" "s" "t" "u" "v" "w" "x" "y" "z" "other")
for alphabet in ${alphabets[@]};
do
	rm $base_dir/"packagelists/"$alphabet"packages.json"
	scrapy crawl spider -a start_url=$base_url$alphabet$extension -o $base_dir/"packagelists/"$alphabet"packages.json" -t json	
done
for alphabet in ${alphabets[@]};
do
	cd $base_dir
	cd programs
	python packagemanager.py $base_dir/"packagelists/"$alphabet"packages.json" $base_dir/"manpages/"$alphabet"/"
	python manpagefetcher.py $alphabet diffFile.json $base_dir/"manpages"
	rm diffFile.json
done
