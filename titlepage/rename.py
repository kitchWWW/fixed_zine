import os

def doAndSay(com):
	print(com)
	os.system(com)


targetfolder = "allmonkey/images"

count = 0

for fname in os.listdir(targetfolder):
	if ".DS_Store" in fname:
		continue
	# print(fname)
	fname = fname.replace(" ","\\ ").replace("(","\\(").replace(")","\\)")
	# extension = fname.split(".")[1]
	doAndSay("mv "+targetfolder+"/"+fname+" " +targetfolder+"/"+str(count)+".png")
	count+=1