from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    README = f.read()

setup(
    name='pynasa',
    version='1.0.0',
    description='Python library and command-line utility for the NASA API (https://api.nasa.gov/)',
    long_description=README,
    long_description_content_type='text/x-rst',
    author='Giovanny Jimenez',
    author_email='gjimenezdeza@gmail.com',
    url='https://github.com/techatlasdev/pynasa',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'pynasa=pynasa.cli.commands:main',
        ],
    },
    keywords=['NASA', 'API', 'space', 'astronomy', 'science', 'data', 'python'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Astronomy',
    ],
)
