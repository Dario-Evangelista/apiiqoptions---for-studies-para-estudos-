from setuptools import setup, find_packages
from apibroker.version_control import api_version

setup(
    name="apibrokerr",
    version=api_version,
    packages=find_packages(),
    include_package_data=True,
    description="Versão modificada",
    long_description="Best IQ Option API for python",
    url="https://github.com/Dario-Evangelista/",
    author="Dario",
    author_email="Darioaraujo44@gmail.com",
    zip_safe=False
)
