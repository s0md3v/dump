import io
from os import path
from setuptools import setup, find_packages

pwd = path.abspath(path.dirname(__file__))
with io.open(path.join(pwd, 'README.md'), encoding='utf-8') as readme:
    desc = readme.read()

setup(
    name='json2paths',
    version=__import__('json2paths').__version__,
    description='converts json keys to paths for bruteforcing',
    long_description=desc,
    long_description_content_type='text/markdown',
    author='s0md3v',
    license='Apache-2.0 License',
    url='https://github.com/s0md3v/json2paths',
    download_url='https://github.com/s0md3v/dump/tree/master/json2paths',
    packages=find_packages(),
    classifiers=[
        'Topic :: Security',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'j2p = json2paths.main:main'
        ]
    },
    keywords=['pentesting', 'security']
)