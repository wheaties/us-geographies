from setuptools import setup

setup(
    entry_points={
        'console_scripts': [
            'us-geographies = main:cli'
        ],
    },
)
