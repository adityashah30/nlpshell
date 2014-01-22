import json
import nltk
import urllib
import sys

def __main__():
	alphabet = sys.argv[1]
	packageFile = sys.argv[2]
	filepath = sys.argv[3]
	base_url = "http://linux.die.net/man/"
	try:
		with open(packageFile,'r') as jsonfile:
			dictlist = json.load(jsonfile)
		if dictlist == []:
			print "Man pages for \""+alphabet+"\" up to date..."
		else:
			for dict1 in dictlist:
				filename = dict1["title"][0]+"("+dict1["link"][0].split("/")[0]+")"
				url = dict1["link"][0]
				url = base_url+url
				htmldata = urllib.urlopen(url).read()
				textdata = nltk.clean_html(htmldata)
				with open(filepath+"/"+alphabet+"/"+filename,'w') as outputFile:
					outputFile.write(textdata)
				print "Man Page for "+filename+" Fetched..."
			print "All Man pages for \""+alphabet+"\" Fetched..."
	except ValueError:
		print "Man pages for \""+alphabet+"\" up to date..."

if __name__ == "__main__":
	__main__()