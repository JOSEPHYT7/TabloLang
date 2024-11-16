# setup.py
from setuptools import setup, find_packages

setup(
    name='TabloLang',
    version='0.1.0',
    description='A simple backend programming language for storing HTML data in tabular form.',
    author='Yerramala Joseph',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'lxml',
    ],
    entry_points={
        'console_scripts': [
            'tablolang=src.interpreter:main',
        ],
    },
)
