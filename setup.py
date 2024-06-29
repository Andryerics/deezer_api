# setup.py

from setuptools import setup, find_packages

setup(
    name='deezer_api',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.0'
    ],
    include_package_data=True,
    author='Andry RL',
    author_email='andryerics@gmail.com',
    description='Une bibliothèque pour interagir avec l\'API Deezer',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Andryerics/deezer_api',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
