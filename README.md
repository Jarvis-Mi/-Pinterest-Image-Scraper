# Pinterest Scraper

A powerful Python tool to scrape and download images from Pinterest using Playwright. This tool extracts image URLs from any Pinterest board and downloads them concurrently with multi-threading, offering both headless and standard browser modes.

## Features

- **Image Scraping:** Extract image URLs from any Pinterest board.
- **Concurrent Downloads:** Download images efficiently using multi-threading.
- **Command-Line Interface (CLI):** Simple and user-friendly CLI for quick operations.
- **Headless Mode:** Option to run in headless mode for faster, resource-efficient scraping.
- **Modular Design:** Well-organized code structure for easy customization and extension.

## Installation

### Prerequisites

- Python **3.6+**
- Google Chrome or Chromium installed
- Playwright dependencies installed

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Jarvis-Mi/-Pinterest-Image-Scraper.git
   cd pinterest_scraper
     ```
2. **Install dependencies:**
      ```bash
         pip install -e .
         playwright install
      ```
##   Usage
###   Run the scraper using:

**Run the scraper using:**
```bash
python  -m pinterest_scraper.cli <username> <tag> <num_images> [--headless]
```
##   Arguments:
1. <username>: Pinterest username or profile name.
2. <tag>: Tag or board name.
3. <num_images>: Number of images to download.
4. [--headless]: (Optional) Run the browser in headless mode.

##   Example:
```bash
python -m pinterest_scraper.cli exampleuser travel 10 --headless
```
***This command scrapes and downloads 20 images from the "travel" board of user "exampleuser" in headless mode.***

### Now that your package has been successfully installed, you can test it by installing it using pip and running a simple script to verify that it works.

## Usage
**Install the package:**
```bash
pip install auto-pi-download
```
**Test the package:**
## Once installed, you can test the package by writing a simple script. The package includes a module to download Pinterest images (based on the package name), you can use the following sample code to test it:
```bash
from pinterest_scraper import get_image_urls, download_images
pinterest_url = "https://www.pinterest.com/exampleuser/board/"  
num_images = 10  

img_urls = get_image_urls(pinterest_url, num_images=num_images)

if not img_urls:
    print("No images found.")
else:
    print(f"Found {len(img_urls)} images.")
    download_images(img_urls, "exampleuser")  
    print("Download completed.")


```
