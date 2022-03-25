from setuptools import setup

version = "0.0.1"

readme = ""

with open("README.md") as file:
    readme = file.read()

setup(
    name="wgtanks",
    packages=["wgtanks"],
    version=version,
    description="Unofficial World of Tanks API Wrapper in Python",
    long_description=str(readme),
    author="Androdameda, Sep., enderjoker",
    author_email="113euro@gmail.com",
    url="https://github.com/TiberSe/WorldofTanks-API.py",
    include_package_data=True,
    keywords=["wot", "world of tanks"],
    classifiers=[
        "Programming Language :: Python :: 3.7"
    ],
    install_requires=[
        "requests"
    ]
)
