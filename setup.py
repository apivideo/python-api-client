"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""

import pathlib
from setuptools import setup, find_packages  # noqa: H301

NAME = "api.video"
VERSION = "1.4.7"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "python_dateutil >= 2.5.3",
  "setuptools >= 21.0.0",
  "urllib3 >= 1.25.3"
]

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


setup(
    name=NAME,
    version=VERSION,
    description="api.video Python API client",
    author="api.video ecosystem team",
    author_email="ecosystem@api.video",
    url="https://github.com/apivideo/api.video-python-client",
    keywords=["api.video", "sdk", "api client", "video", "live", "hls"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description=README,
    long_description_content_type="text/markdown",
)
