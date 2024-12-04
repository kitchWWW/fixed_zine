import random 
import os

def doAndSay(com):
	print(com)
	os.system(com)


for i in range(10):
	ii = str(i)
	ns = random.sample(range(4),3)
	ns.insert(0,"start")
	random.shuffle(ns)
	# doAndSay("magick fixed/"+n+".png -gravity center -smush 100 out/"+n+"title.png")
	# doAndSay("convert -resize 500% out/"+n+"title.png out/"+n+"bigger.png")
	doAndSay("magick images/"+str(ns[0])+".png images/"+str(ns[1])+".png -gravity center +smush 20 out/a.png")
	doAndSay("magick images/"+str(ns[2])+".png images/"+str(ns[3])+".png -gravity center +smush 20 out/b.png")
	doAndSay("magick out/a.png out/b.png -gravity center -smush 20 out/"+ii+"imgs.png")
	doAndSay("convert -resize 120%  -define png:color-type=6 monkeystitle.png monkeystitlesmol.png")
	# doAndSay("magick images/"+str(ns[0])+".png images/"+str(ns[1])+".png images/"+str(ns[2])+".png  -gravity center -smush 20 out/"+ii+"imgs.png")
	doAndSay("convert -resize 400% out/"+ii+"imgs.png out/"+ii+"imgsbig.png")
	doAndSay("magick monkeystitlesmol.png out/"+ii+"imgsbig.png  -gravity center -smush 20 -define png:color-type=6  out/"+ii+"page.png")
	doAndSay("convert out/"+ii+"page.png -transparent white  out/"+ii+"print.png")
	# doAndSay("convert -append out/"+n+"title.png name/"+n+".png  out/"+n+".png")

# exit()

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