from setuptools import setup, find_packages
import os
from setuptools.command.install import install

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        # Make decode-config executable
        os.chmod(os.path.join(self.install_lib, 'tasmonator', 'bin', 'decode-config'), 0o755)

setup(
    name='tasmonator',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
        'requests',
    ],
    include_package_data=True,
    package_data={
        '': ['bin/decode-config'],
    },
    entry_points={
        'console_scripts': [
            'tasmonator = tasmonator.cli:main',
        ],
    },
    cmdclass={
        'install': PostInstallCommand,
    },
)
