import os
from setuptools import setup


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='stellar_identicon',
    version='0.1',
    description='Python stellar address identicon generator',
    url='https://github.com/Lobstrco/stellar-identicon-py',
    author='Nikita Haradzetski',
    author_email='nikita.g@razortheory.com',
    packages=['stellar_identicon'],
    install_requires=['randomcolor>=0.4,<0.5', 'pydenticon>=0.3,<0.4', ],
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)