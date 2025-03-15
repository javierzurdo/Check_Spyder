from setuptools import setup

setup( 
    name='check_spyder',
    version='0.1',
    packages=['check_spyder'],
    description='Library to detect if you are using Spyder IDE or not.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Javier S. Zurdo',
    url='',
    install_requires=['os'],
)