from setuptools import setup, find_packages

"""
https://python-packaging.readthedocs.io/en/latest/minimal.html
https://packaging.python.org/en/latest/specifications/declaring-project-metadata/

python setup.py register
python setup.py register sdist upload

https://packaging.python.org/en/latest/tutorials/packaging-projects/

Once:

$ python3 -m pip install --upgrade build
$ python3 -m pip install --upgrade twine

Each iteration:

$ python3 -m build
$ python3 -m twine upload --repository pypi dist/*

"""

setup(
    name="rdapy",
    version="1.0.4",
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
        "rdapy.minority",
        "rdapy.partisan",
        "rdapy.splitting",
        "rdapy.rate",
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
