import sys
import json
import subprocess

def __main__():
	packageFile = open(sys.argv[1], 'r')
	dirpath = sys.argv[2]
	difflist = []
	lslist = []

	ls = subprocess.Popen(['ls', dirpath], stdout=subprocess.PIPE)
	op = ls.communicate()[0]
	for item in op.splitlines():
		lslist.append(item)
	lslist.sort()
	try:
		packagelist = json.load(packageFile)
		packageFile.close()
		packagelen = len(packagelist)
		lslen = len(lslist)
		if lslen == 0:
			difflist = packagelist
		packageptr = lsptr = 0
		while packageptr < packagelen and lsptr < lslen:
			# print lslist[lsptr]
			# print packagelist[packageptr]["title"][0]+"("+packagelist[packageptr]["link"][0].split("/")[0]+")"
			# print "----------------------------------"
			if lslist[lsptr] == packagelist[packageptr]["title"][0]+"("+packagelist[packageptr]["link"][0].split("/")[0]+")":
				lsptr += 1
				packageptr += 1
			elif lslist[lsptr] < packagelist[packageptr]["title"][0]+"("+packagelist[packageptr]["link"][0].split("/")[0]+")":
				lsptr += 1
			else:
				difflist.append(packagelist[packageptr])
				packageptr += 1
		if(packagelen > lslen):
			while packageptr < packagelen:
				difflist.append(packagelist[packageptr])
				packageptr += 1

	except ValueError:
		difflist = lslist

	with open('diffFile.json', 'w') as diffFile:
			json.dump(difflist, diffFile)

if __name__ == "__main__":
	__main__()