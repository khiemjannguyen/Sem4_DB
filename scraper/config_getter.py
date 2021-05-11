import os, sys, json


PATH = os.path.dirname(os.path.abspath(__file__))
def get_config(filename):
    with open(os.path.join(PATH, "configs/" + filename), "r") as config_json:
        configs = json.load(config_json)
        config_json.close()
        return configs
