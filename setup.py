from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in orfelo_app/__init__.py
from orfelo_app import __version__ as version

setup(
	name="orfelo_app",
	version=version,
	description="Country Indonasia orfelo.erpnext.com First contain Receivable accounts reports with custom field",
	author="Muhammad Zubair",
	author_email="experterp771@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
