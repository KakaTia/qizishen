import pytest
import yaml
from selenium import webdriver

def get_memberinfo():
    with open('TestWeWork/memberinfo.yaml') as e:
        tatols = yaml.safe_load(e)
        return tatols