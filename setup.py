from setuptools import setup, find_packages

setup(
    name='tasmota_config_tool',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'tasmota-config-tool = tasmota_config_tool.cli:main',
        ],
    },
)
