# pinterest_scraper/cli.py
import argparse
from .scraper import get_image_urls
from .downloader import download_images

def parse_args():
    parser = argparse.ArgumentParser(description="Pinterest Image Scraper")
    parser.add_argument("username", type=str, help="Pinterest username or page")
    parser.add_argument("tag", type=str, help="Board tag or name")
    parser.add_argument("num_images", type=int, help="Number of images to download")
    parser.add_argument("--headless", action="store_true", help="Run headless (without GUI)")
    return parser.parse_args()

def main():
    args = parse_args()
    pinterest_url = f"https://www.pinterest.com/{args.username}/{args.tag}/"
    print(f"Getting started with URL:{pinterest_url}")

    img_urls = get_image_urls(pinterest_url, num_images=args.num_images)
    if not img_urls:
        print("Image not found. Please try again.")
        return

    print(f" Number of images found: {len(img_urls)}")
    download_images(img_urls, args.username)
    print("\n The image download has finished.")

if __name__ == "__main__":
    main()
