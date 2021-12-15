from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in app1/__init__.py
from app1 import __version__ as version

setup(
	name="app1",
	version=version,
	description="app",
	author="pub",
	author_email="app",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
