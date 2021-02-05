"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open

here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

requirements = []
with open(path.join(here, "requirements.txt"), encoding="utf-8") as f:
    for line in f:
        line = line.split('#', 1)[0].strip()
        if not line:
            continue
        requirements.append(line)

setup(
    name="glaucoma_ML",
    version="0.0.1",
    description="investigate wether ML can be used to grade VCDR of eye images , correpsonding to liklehook of glaucoma",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaxKelsen/Glaucoma-Phenotype-ML-estimation",
    author="Kaiah Steven",
    author_email="kaiah.steven@maxkelsen.com",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=requirements,  # Optional
    extras_require={}, # Optional
    package_data={}, # Optional
    data_files=[],  # Optional
    entry_points={}, # Optional
    project_urls={} # Optional
)
