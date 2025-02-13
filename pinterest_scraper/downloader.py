# pinterest_scraper/downloader.py
import urllib.request
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

def download_image(img_url, output_path):
    try:
        urllib.request.urlretrieve(img_url, output_path)
        print(f"Downloaded: {output_path.name}", end="\r")
    except Exception as e:
        print(f"Error Downloading {output_path.name}: {e}")

def download_images(img_urls, name_img):
    output_dir = Path("downloaded_images") / name_img
    output_dir.mkdir(parents=True, exist_ok=True)

    with ThreadPoolExecutor(max_workers=10) as executor:
        for index, img_url in enumerate(img_urls):
            file_name = output_dir / f"{name_img}{index+1}.jpg"
            executor.submit(download_image, img_url, file_name)
