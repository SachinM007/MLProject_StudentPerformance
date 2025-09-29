#Using setup.py our ml project can be used as a package and can be deployed and implemented elsewehere

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    """
    this function returns list of requiremments
    
    """

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
        return requirements
    
    
#contains metadata information about the project
setup(
    name='StudentPerformance ML Project',
    version='0.0.1',
    author='Sachin',
    author_email='bsachinmiryala@gmail.com',
    packages=find_packages() , #checks all files having constructor(init.py) and considers them as packages and builds them, once they are build we can use them to import
    install_requires=get_requirements('requirements.txt')
) 