"""
A package to train and infer DDPG Tensorflow 2
"""

import setuptools
from setuptools import find_packages

PACKAGE_NAME: str = "ddpg-tf2"

REQUIRED = [
  "tensorflow-gpu==2.7.2",
  "tqdm==4.37.0",
  "gym==0.17.2",
  "box2d-py==2.3.8",
  "matplotlib==3.1.1",
  "pytest==2.9.1",
  "bandit==1.7.4",
  "pylint==2.14.4"
]

setuptools.setup(
  name=PACKAGE_NAME,
  version='1.0.0',
  description="""
    Simple yet effective DDPG implementation for continuous action space,
    written in Tensorflow 2
  """,
  author="Samuel Matthew Koesnadi",
  author_email="samuelmat19@gmail.com",
  install_requires=REQUIRED,
  packages=find_packages(),
  entry_points = {
    'console_scripts': [f'{PACKAGE_NAME}=src.command_line:main'],
  }
)
