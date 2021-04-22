#!/usr/bin/env python

# Inspired by:
# https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/

import codecs
import os
import re

from setuptools import find_packages, setup

# PROJECT SPECIFIC

NAME = "exoplanet"
PACKAGES = find_packages(where="src")
META_PATH = os.path.join("src", "exoplanet", "__init__.py")
CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
]
INSTALL_REQUIRES = ["exoplanet-core[pymc]>=0.1", "astropy>=3.1"]
EXTRA_REQUIRE = {
    "test": [
        "scipy",
        "pytest",
        "pytest-cov>=2.6.1",
        "pytest-env",
        "batman-package",
    ],
    "docs": [
        "sphinx>=1.7.5",
        "sphinx-typlog-theme",
        "rtds_action",
        "nbsphinx",
        "ipython",
    ],
    "tutorials": [
        "jupytext>1.7.0",
        "jupyter",
        "nbconvert",
        "matplotlib",
        "corner",
        "lightkurve",
        "pymc3-ext>=0.1.0",
    ],
}

# END PROJECT SPECIFIC


HERE = os.path.dirname(os.path.realpath(__file__))


def read(*parts):
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


def find_meta(meta, meta_file=read(META_PATH)):
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta), meta_file, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


if __name__ == "__main__":
    setup(
        name=NAME,
        use_scm_version={
            "write_to": os.path.join(
                "src", NAME, "{0}_version.py".format(NAME)
            ),
            "write_to_template": '__version__ = "{version}"\n',
        },
        author=find_meta("author"),
        author_email=find_meta("email"),
        maintainer=find_meta("author"),
        maintainer_email=find_meta("email"),
        url=find_meta("uri"),
        license=find_meta("license"),
        description=find_meta("description"),
        long_description=read("README.md"),
        long_description_content_type="text/markdown",
        packages=PACKAGES,
        package_dir={"": "src"},
        include_package_data=True,
        python_requires=">=3.6",
        install_requires=INSTALL_REQUIRES,
        extras_require=EXTRA_REQUIRE,
        classifiers=CLASSIFIERS,
        zip_safe=False,
    )
