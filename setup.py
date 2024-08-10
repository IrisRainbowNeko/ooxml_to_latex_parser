# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='ooxml_to_latex',
    version="0.1",
    packages=["ooxml_to_latex"],
    url='https://github.com/IrisRainbowNeko/ooxml_to_latex_parser',
    license='MIT',
    author='IrisRainbowNeko',
    author_email='rainbow-neko@outlook.com',
    description='Open office xml to latex parser ',
    install_requires=['lxml'],

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='>=3.8',
)
