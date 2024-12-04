import os

def doAndSay(com):
	print(com)
	os.system(com)


for i in range(100):
	n = str(i)
	title = "titleBits/out/"+n+"print.png"
	startCount = i*6
	allScoreNames  = []
	for z in range(6):
		allScoreNames.append("newexports/export-"+str((i*6)+z+1).zfill(4)+".png")
	scoreString = " ".join(allScoreNames)
	doAndSay("convert "+title+" " +scoreString+" backdata/"+str(i)+".png pdfOuts/"+str(i)+"out.pdf")
	doAndSay("pdfbook2 --paper=letterpaper --no-crop --short-edge --outer-margin=1 --inner-margin=1 --top-margin=1 --bottom-margin=1 \"pdfOuts/"+str(i)+"out.pdf\"")