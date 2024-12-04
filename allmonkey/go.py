import subprocess
import os

# Base URL for the images
base_url = "http://www.djsphotography.co.uk/images/Rainforest/Crested-Black-Macaque-"

# Directory to save the images
output_dir = "images"
os.makedirs(output_dir, exist_ok=True)

# Loop to download images
for i in range(201):  # From 0 to 200
    file_name_cr = f"{output_dir}/Crested-Black-Macaque-{i}-cr.jpg"
    file_name = f"{output_dir}/Crested-Black-Macaque-{i}.jpg"
    url_cr = f"{base_url}{i}-cr.jpg"
    url = f"{base_url}{i}.jpg"
    
    # Try the version with "-cr.jpg"
    print(f"Trying: {url_cr}")
    result_cr = subprocess.run(
        ["curl", "--fail", "-o", file_name_cr, url_cr],
        capture_output=True,
        text=True
    )
    
    if result_cr.returncode == 0:  # If download is successful
        print(f"Downloaded: {file_name_cr}")
        continue  # Skip the next attempt
    else:
        print(f"Failed: {url_cr}, trying {url}")
    
    # Try the version with ".jpg"
    result = subprocess.run(
        ["curl", "--fail", "-o", file_name, url],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:  # If download is successful
        print(f"Downloaded: {file_name}")
    else:
        print(f"Failed to download both versions: {url_cr} and {url}")

print("Download process complete.")
