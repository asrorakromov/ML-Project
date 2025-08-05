from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    "This function will return the list of requirements"
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[i.replace("\n", " ")for i in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements



setup(
name='ML Project',
version='0.0.1',
author='Asror',
author_email='asrorakromov989@gmail.com',
packeges=find_packages(),
install_requires=get_requirements('requirements.txt')
)