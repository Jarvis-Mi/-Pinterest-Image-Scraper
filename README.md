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
pinterest-scraper <username> <tag> <num_images> [--headless]
```
##   Arguments:
1. <username>: Pinterest username or profile name.
2. <tag>: Tag or board name.
3. <num_images>: Number of images to download.
4. [--headless]: (Optional) Run the browser in headless mode.

##   Example:
```bash
pinterest-scraper exampleuser travel 20 --headless
```
***This command scrapes and downloads 20 images from the "travel" board of user "exampleuser" in headless mode.***

###   Project Structure :
```bash
pinterest_scraper/
├── pinterest_scraper/
│   ├── __init__.py          # Package initialization and metadata
│   ├── cli.py               # Command-line interface implementation
│   ├── downloader.py        # Functions for downloading images
│   └── scraper.py           # Functions for scraping image URLs
├── setup.py                 # Setup script for packaging and installation
├── README.md                # Project documentation
└── LICENSE                  # License file
```
