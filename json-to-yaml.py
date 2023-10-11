# A straightforward script that converts JSON to YAML.

import json
import yaml

# Load JSON data from a file
with open('C:/Users/laytoja/OneDrive - EY/Documents/Projects/ASS3T/enterprise-attack.json', 'r') as json_file:
    data = json.load(json_file)

# Convert JSON data to YAML
with open('C:/Users/laytoja/OneDrive - EY/Documents/Projects/ASS3T/enterprise-attack-converted.yaml', 'w') as yaml_file:
    yaml.dump(data, yaml_file, default_flow_style=False)

