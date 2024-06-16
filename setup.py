from setuptools import setup, find_packages

setup(
    name='tasmonator',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'tasmonator = tasmonator.cli:main',
        ],
    },
)
