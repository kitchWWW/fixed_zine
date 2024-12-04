import os

def doAndSay(com):
    print(com)
    os.system(com)

# Specify the base folder (e.g., 'bits', 'bops')
base_folder = "msolbits"
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
        pandoc_options = ' --template=latex-pandoc.template -V fontsize=8pt -V geometry:margin=0.5in -V geometry:papersize="{5.5in,8in}"'

        # Create the pandoc command
        pandoc_command = "pandoc " + txt_path + " " + pandoc_options + " -o " + pdf_path

        # Run the command using doAndSay
        doAndSay(pandoc_command)

# Clean up any temporary files if needed (example: removing intermediate files)
# doAndSay("rm -f some_temp_files*")
