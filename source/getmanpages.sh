#/bin/bash
base_dir=$PWD
cd Spider
base_url="http://linux.die.net/man/"
extension=".html"
declare -a alphabets=("a" "b" "c" "d" "e" "f" "g" "h" "i" "j" "k" "l" "m" "n" "o" "p" "q" "r" "s" "t" "u" "v" "w" "x" "y" "z" "other")
for alphabet in ${alphabets[@]};
do
	scrapy crawl spider -a start_url=$base_url$alphabet$extension -o $base_dir/"manpages/"$alphabet"/"$alphabet"packages.json" -t json	
done
for alphabet in ${alphabets[@]};
do
	cd $base_dir
	cd programs
	python manpagefetcher.py $alphabet $base_dir/"manpages/"$alphabet"/"$alphabet"packages.json"
	cd manpages_temp
	mv * $base_dir/"manpages/"$alphabet"/"
	echo "All Man Pages for \""$alphabet"\" fetched..."
done
