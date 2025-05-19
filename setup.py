from setuptools import setup, find_packages

"""
https://python-packaging.readthedocs.io/en/latest/minimal.html
https://packaging.python.org/en/latest/specifications/declaring-project-metadata/

python setup.py register
python setup.py register sdist upload

"""

setup(
    name="rdapy",
    version="2.1.0",
    description="Redistricting analytics in Python",
    url="https://github.com/dra2020/rdapy",
    author="alecramsay",
    author_email="alec@davesredistricting.org",
    license="MIT",
    packages=[
        "rdapy",
        "rdapy.compactness",
        "rdapy.compactness.pypoly",
        "rdapy.equal",
        "rdapy.graph",
        "rdapy.minority",
        "rdapy.partisan",
        "rdapy.splitting",
        "rdapy.rate",
        "rdapy.utils",
        "rdapy.score",
        "rdapy.score.utils",
    ],
    install_requires=[
        "Fiona",
        "geographiclib",
        "geopandas",
        "libpysal",
        "nptyping",
        "numpy",
        "pandas",
        "pyproj",
        "pytest",
        "scipy",
        "shapely",
    ],
    zip_safe=False,
)
