#!/usr/bin/env python3
##############################################################################%
import requests
import subprocess
import configparser

BASE_URL = 'https://api.cloudflare.com/client/v4/'


def clear_screen():
    subprocess.run(["clear"])


def cf_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    zone_id = config['zone']['id']
    account_id = config['account']['id']
    global_api_key = config['api']['global_key']
    origin_ca_key = config['api']['origin_ca_key']
    api_token = config['api']['token_admin_all']
    return zone_id, account_id, global_api_key, origin_ca_key, api_token


def test_api_token(token):
    subprocess.run([
    'curl',
    '-X',
    'GET',
    'https://api.cloudflare.com/client/v4/user/tokens/verify',
    '-H',
    f'Authorization: Bearer {token}',
    '-H',
    'Content-Type:application/json',
    ])

def curl_get_dns_records(zone_id, token):
    subprocess.run([
        'curl',
        '--request',
        'GET',
        '--url',
        f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records',
        '--header',
        f'X-Auth-Email: {token}',
        '--header',
        'Content-Type: application/json',
    ])

def get_dns_records(zone_id, token):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Email": token,
    }
    return requests.request("GET", url, headers=headers)


def get_user_data(token):
    url = BASE_URL + 'user'
    auth = 'Authorization: Bearer ' + token
    subprocess.run([
        'curl',
        '-X',
        'GET',
        url,
        '-H',
        'Content-Type:application/json',
        '-H',
        auth,
    ])

cf_zid, cf_aid, cf_gapi_key, cf_oca_key, cf_api_token = cf_config('configs/cf.ini')


#print(test_api_token(cf_api_token))
#print(curl_get_dns_records(cf_zid, cf_api_token))
print(get_user_data(cf_api_token))
#print("requests.request(\"GET\", " + url + ",  + headers)")
#print("\n\nresponse:\n")
#print(response.text)
#
#print("\n==================================================")
#print("\nZone ID: ")
#print(zone_id)
#print(len(zone_id))
#print("\nAPI Token:")
#print(api_token)
#print(len(api_token))
#print("\nURL: ", url)
#print("====================================================\n")


#    "Authorization": f"Bearer ${api_token}"
