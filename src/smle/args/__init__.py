import yaml

def read_configuration_file(config_file:str ="smle.yaml"):

    with open(config_file) as f:
        args = yaml.safe_load(f)

    return args