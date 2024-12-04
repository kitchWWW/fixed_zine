from PIL import Image, ImageDraw, ImageFont
import random

for i in range(20):

	# Create a new blank image with white background
	width, height = 3500, 1200
	image = Image.new("RGB", (width, height), "white")

	# Initialize ImageDraw
	draw = ImageDraw.Draw(image)

	# Load a font
	try:
	    font = ImageFont.truetype("./res/gar.ttf", 100)
	except IOError:
	    font = ImageFont.load_default()

	aboutarray = ["copyright law", 'generative art', 'artificial intelligence', 'humanness', 'capitalism']
	random.shuffle(aboutarray)
	# Define the text
	text = "a zine about\n\n" + ("\n".join(aboutarray))+"\n\nand what we should do about it all"
	lines = text.split("\n")

	# Calculate the size of the text
	text_width = max(draw.textlength(line, font=font) for line in lines)
	text_height = font.size * len(lines)

	# Calculate the position to center the text
	position = ((width - text_width) // 2, (height - text_height) // 2)

	# Add text to image
	draw.multiline_text(position, text, fill="black", font=font, align="center")

	# Save the image
	image.save("bitbit/"+str(i)+".png")

	# Display the image
	# image.show()
