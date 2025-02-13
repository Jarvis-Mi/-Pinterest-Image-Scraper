from setuptools import setup, find_packages

setup(
    name="jarvis-mi-pinterest-scraper",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'playwright',
    ],
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
