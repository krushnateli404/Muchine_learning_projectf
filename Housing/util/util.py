import yaml
from Housing.exception import HousingException
import os,sys

def read_yaml_file(file_path:str):
    """Read yaml file and return contents as dictionary
    file_path = str
    """
    try:
        with open(file_path,"r") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException (e,sys) from e