from setuptools import setup,find_packages
from typing import List

#Declaring variables for setup functions

PROJECT_NAME = "Housing-predictor"
VIRSION = "0.0.3"
AUTHOR = "Krushna Teli"
DESCRIPTION = "This is a fsds new batch machine learnig project"
# PACKAGES = ["Housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_equirements_list()->List[str]:
    """
    Description:This function is going to return list of requirement mention in requirment.txt file

    return this function is going to return #list which contain name of libraries mentioned in requirements.txt file
    
    """

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()


setup(
    name = PROJECT_NAME ,
    version=VIRSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires = get_equirements_list()
)


if __name__ == "__main__":
    print(get_equirements_list())