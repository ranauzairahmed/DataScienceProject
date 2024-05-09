from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path) -> List[str]:
 requirements = []
 with open(file_path) as f:
  requirements = f.readlines()
  [req.replace('\n', '') for req in requirements]
 return requirements


setup(
 name='Data Science Project',
 version='1.0.0',
 author='Uzair',
 author_email='ranauzairahmed.official@gmail.com',
 packages=find_packages(),
 install_requires = get_requirements('requirements.txt')
)