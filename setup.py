from setuptools import setup, find_packages

setup(
    name='html2docx',
    version='1.0.0',
    url='https://github.com/1qubit-org/html2docx',
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4==4.12.2",
        "python-docx==1.1.0"
    ],
)
