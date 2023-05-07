from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    #this fuction will return requirements

    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        requirements =  [req.replace("\n","")for req in requirements]


        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name = 'mlproject',
    version = '0.0.1',
    author =  'Rana',
    author_email = 'widodo.gembel123@gmaill.com',
    packages = find_packages(),
    intsall_requires = get_requirements('requirements.txt')


)