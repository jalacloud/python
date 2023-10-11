# A straightforward script that converts JSON to YAML.

import json
import yaml

# Load JSON data from a file
with open('{{ INPUT_FILEPATH }}', 'r') as json_file:
    data = json.load(json_file)

# Convert JSON data to YAML
with open('{{ OUTPUT_FILEPATH }}', 'w') as yaml_file:
    yaml.dump(data, yaml_file, default_flow_style=False)

