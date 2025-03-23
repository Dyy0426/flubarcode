from setuptools import setup, find_packages

setup(
    name="flubarcode",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'pandas',
        'biopython',
        'scikit-learn',
        'weblogo'
    ],
    entry_points={
        'console_scripts': [
            'flubarcode = flubarcode.cli:main'
        ]
    },
    author="DYY",
    description="Barcode sequencing data processing toolkit",
    url='https://github.com/Dyy0426/flubarcode.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
