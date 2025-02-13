from setuptools import setup, find_packages

setup(
    name="auto_pi_download",
    version="0.01",
    packages=find_packages(),
    install_requires=[
        'playwright',
    ],
    entry_points={
        'console_scripts': [
            'download_images_from_pinterest = pinterest_scraper.cli:main',  
        ],
    },
    description="A simple Pinterest image scraper",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Mahdi Ajami",
    author_email="gw2.fighter@gmail.com",
    url="https://github.com/Jarvis-Mi/-Pinterest-Image-Scraper",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
