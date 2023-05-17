from setuptools import setup, find_packages

"""
python setup.py register
python setup.py register sdist upload
"""

setup(
    name="rdapy",
    version="1.0.2",
    description="Redistricting analytics in Python",
    url="https://github.com/dra2020/rdapy",
    author="alecramsay",
    author_email="alec@davesredistricting.org",
    license="MIT",
    packages=[
        "rdapy",
        "rdapy.compactness",
        "rdapy.equal",
        "rdapy.graph",
        "rdapy.partisan",
        "rdapy.splitting",
    ],
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
