from setuptools import setup, find_packages


setup(
  name="test_package",
  version="0.0.1",
  author="Tonye Jack",
  author_email="jtonye@ymail.com",
  install_requires=['requests', 'django'],
  packages=find_packages(),
)
