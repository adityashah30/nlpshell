import json
import nltk
import urllib
import sys

def __main__():
	alphabet = sys.argv[1]
	packageFile = sys.argv[2]
	base_url = "http://linux.die.net/man/"
	with open(packageFile,'r') as jsonfile:
		dictlist = json.load(jsonfile)
	for dict1 in dictlist:
		filename = dict1["title"][0]
		url = dict1["link"][0]
		url = base_url+url
		htmldata = urllib.urlopen(url).read()
		textdata = nltk.clean_html(htmldata)
		with open("manpages_temp/"+filename,'w') as outputFile:
			outputFile.write(textdata)
		print "Man Page for "+filename+" Fetched..."

if __name__ == "__main__":
	__main__()