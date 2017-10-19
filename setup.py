# coding=utf-8
from setuptools import setup

setup(
    name='codegen',
    version = '1.0',
    description='Extension to ast that allow ast -> python code generation.',
    url='http://github.com/CensoredUsername/codegen',
    download_url='https://github.com/CensoredUsername/codegen',
    keywords='ast codegen',
    platforms='any',
    zip_safe=False,
    license='BSD',
    install_requires = [],
    py_modules=['codegen'],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
