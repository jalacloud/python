import requests
import urllib



# define palo firewall variables //

pa_ip = "fw-ip-address"
pa_user = ''
pa_pass = ''


# panos API call to generate API key
panos_api_key = requests.get(f'https://{pa_ip}/api/?type=keygen&user={pa_user}&password={pa_pass}', verify=False)
print(panos_api_key.text)
