# setup.py
from setuptools import setup, find_packages

setup(
    name="pinterest_scraper",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "playwright",
    ],
    entry_points={
        "console_scripts": [
            "pinterest-scraper=pinterest_scraper.cli:main"
        ]
    },
    author="نام شما",
    description="A Pinterest image scraper using Playwright",
)
