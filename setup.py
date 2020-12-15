import os
from setuptools import setup, find_packages

README_PATH = "README.md"
LONG_DESCRIPTION = ""

if os.path.exists(README_PATH):
    with open(README_PATH) as readme:
        LONG_DESCRIPTION = readme.read()


setup(
    name="gs_convert",
    version="0.0.1",
    author="Rogerio Santos",
    author_email="rogeriosan4@gmail.com",
    description="App to use ghostscript file conversion commands",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    license="",
    keywords="",
    url="https://github.com/rogeriosan4/gs_convert",
    packages=find_packages(),
    python_requires='>=3.6, <4',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Operating System :: OS Independent",
    ],
)