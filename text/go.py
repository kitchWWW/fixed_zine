import os
from openai import OpenAI

client = OpenAI(api_key = "")

targetFile = "mplayingdata"

# Read the content from the files
with open(targetFile+'/system.txt', 'r', encoding='utf-8') as system_file:
    system_content = system_file.read()

with open(targetFile+'/user.txt', 'r', encoding='utf-8') as user_file:
    user_content = user_file.read()

# Loop to run 10 times and write output to 1.txt, 2.txt, ..., 10.txt
for i in range(0, 10):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content}
        ]
    )

    output = completion.choices[0].message.content

    # Write output to a file
    filename =targetFile+ f"/out/{i}.txt"
    with open(filename, 'w', encoding='utf-8') as output_file:
        output_file.write(output)

    print(f"Output written to {filename}")


def doAndSay(com):
    print(com)
    os.system(com)

# Specify the base folder (e.g., 'bits', 'bops')
base_folder = targetFile
input_folder = base_folder + "/out"
output_folder = base_folder + "/pdfs"

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all .txt files in the input folder
for filename in sorted(os.listdir(input_folder)):
    if filename.endswith(".txt"):
        # Define full paths for input and output
        txt_path = input_folder + "/" + filename
        pdf_filename = filename.replace(".txt", ".pdf")
        pdf_path = output_folder + "/" + pdf_filename

        # Add any additional pandoc options here
        pandoc_options = ' --template=latex-pandoc.template -V fontsize=10pt -V geometry:margin=0.5in -V geometry:papersize="{5.5in,8in}"'

        # Create the pandoc command
        pandoc_command = "pandoc " + txt_path + " " + pandoc_options + " -o " + pdf_path

        # Run the command using doAndSay
        doAndSay(pandoc_command)

# Clean up any temporary files if needed (example: removing intermediate files)
# doAndSay("rm -f some_temp_files*")
