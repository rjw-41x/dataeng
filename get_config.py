import json
import os

# get config dir
ENV_DIR=os.getenv('REPO_DIR')
config_file_name='app_config.json'

with open( ENV_DIR + "/" + config_file_name ) as conf_file:
    contents = json.load(conf_file)
    conf_dict = {}
    # database
    print(contents['postgres'])
    print(contents['kafka'])
