import os
from setuptools import setup


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name="stellar_identicon",
    version="0.1.1",
    description="Python stellar address identicon generator",
    url="https://github.com/Lobstrco/stellar-identicon-py",
    packages=["stellar_identicon"],
    install_requires=[
        "pydenticon>=0.3,<0.4",
        "stellar-sdk>=3.0.0,<4.0.0",
    ],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
