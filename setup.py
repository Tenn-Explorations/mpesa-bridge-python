import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

packages = find_packages(here / "src")

installed_packages = []

with open(here / "requirements.txt") as f:
    installed_packages = f.read().splitlines()

print(installed_packages)

setup(
    name="mpesa_bridge",
    fullname="mpesa_bridge",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.0.1",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=packages,
    include_package_data=True,
    py_modules=["client"],
    package_dir={"": "src"},
    install_requires=installed_packages,
)
