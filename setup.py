from setuptools import setup

"""
python setup.py register
"""

setup(
    name="rdapy",
    version="1.0",
    description="Redistricting analytics in Python",
    url="https://github.com/dra2020/rdapy",
    author="alecramsay",
    author_email="alec@davesredistricting.org",
    license="MIT",
    packages=["rdapy"],
    install_requires=[
        "attrs",
        "certifi",
        "click",
        "click-plugins",
        "cligj",
        "exceptiongroup",
        "Fiona",
        "geographiclib",
        "iniconfig",
        "munch",
        "nptyping",
        "numpy",
        "packaging",
        "pluggy",
        "pyproj",
        "pytest",
        "scipy",
        "shapely",
        "six",
        "tomli",
    ],
    zip_safe=False,
)
