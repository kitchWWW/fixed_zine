import os

def doAndSay(com):
	print(com)
	os.system(com)


for i in range(10):
	n = str(i)
	doAndSay("magick fixed/"+n+".png -gravity center -smush 100 out/"+n+"title.png")
	doAndSay("convert -resize 500% out/"+n+"title.png out/"+n+"bigger.png")
	doAndSay("convert -resize 300% name/"+n+".png out/"+n+"biggername.png")
	doAndSay("magick out/"+n+"bigger.png bitbit/"+n+".png out/"+n+"biggername.png -gravity center  -smush 300 out/"+n+"page.png")
	doAndSay("convert out/"+n+"page.png -transparent white  out/"+n+"print.png")
	# doAndSay("convert -append out/"+n+"title.png name/"+n+".png  out/"+n+".png")


# exit()

doAndSay("rm out/*title*")
doAndSay("rm out/*bigger*")
doAndSay("rm out/*page*")

bigCom = """
cd out/;
for f in *.png; do
	trimbox=$(convert $f -fuzz 25% -format "%@" info:)
	orig=$trimbox
	first=${trimbox%x*}
	trimbox=${trimbox#*x}
	second=${trimbox%%+*}
	trimbox=${trimbox#*+}
	third=${trimbox%+*}
	fourth=${trimbox#*+}
	#echo "trimbox: $orig first: $first second: $second third: $third fourth:$fourth"
	((first+=50))
	((second+=50))
	((third-=25))
	((fourth-=25))
	trimbox=$first"x"$second"+"$third"+"$fourth
	convert "$f" -crop "$trimbox" +repage "trimmed-$f"
done

"""

# doAndSay(bigCom)