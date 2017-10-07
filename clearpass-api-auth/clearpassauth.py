#!/usr/bin/env python3
#------------------------------------------------------------------------------
#
# Author: @timcappalli, Aruba Security Group
# Organization: Aruba, a Hewlett Packard Enterprise company
#
# Version: 2017.02
#
#
# Copyright (c) Hewlett Packard Enterprise Development LP
# All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.
#
#------------------------------------------------------------------------------

import requests
import json
from configparser import ConfigParser

# configuration file parameters
config = ConfigParser()
config.read('config/params.cfg')

clearpass_fqdn = config.get('ClearPass', 'clearpass_fqdn')
oauth_grant_type = config.get('OAuth2', 'grant_type')
oauth_client_id = config.get('OAuth2', 'client_id')
oauth_client_secret = config.get('OAuth2', 'client_secret')
oauth_username = config.get('OAuth2', 'username')
oauth_password = config.get('OAuth2', 'password')


# validate config
def check_config(clearpass_fqdn, oauth_grant_type, oauth_client_id, oauth_client_secret, oauth_username, oauth_password):
    if not clearpass_fqdn:
        print('Error: ClearPass FQDN must be defined in config file (config/params.cfg)')
        exit(1)
    if not oauth_grant_type:
        print('Error: grant_type must be defined in config file (config/params.cfg)')
        exit(1)
    if not oauth_client_id:
        print('Error: client_id must be defined in config file (config/params.cfg)')
        exit(1)
    if oauth_grant_type == "password" and (not oauth_username or not oauth_password):
        print('Error: username and password must be defined in config file for password grant type (config/params.cfg)')
        exit(1)


def get_access_token(clearpass_fqdn, oauth_grant_type, oauth_client_id, oauth_client_secret, oauth_username, oauth_password):
    url = "https://" + clearpass_fqdn + "/api/oauth"

    headers = {'Content-Type':'application/json'}

    # grant_type: password
    if oauth_grant_type == "password":
        payload = {'grant_type':oauth_grant_type, 'username':oauth_username, 'password':oauth_password, 'client_id':oauth_client_id, 'client_secret':oauth_client_secret}

        try:
            r = requests.post(url, headers=headers, json=payload)
            r.raise_for_status()
        except Exception as e:
            print(e)
            exit(1)

        json_response = json.loads(r.content)

        return json.dumps(json_response)

    # grant_type: password   public client
    if oauth_grant_type == "password" and not oauth_client_secret:
        payload = {'grant_type':oauth_grant_type, 'username':oauth_username, 'password':oauth_password, 'client_id':oauth_client_id}

        try:
            r = requests.post(url, headers=headers, json=payload)
            r.raise_for_status()
        except Exception as e:
            print(e)
            exit(1)

        json_response = json.loads(r.content)

        return json.dumps(json_response)

    # grant_type: client_credentials
    if oauth_grant_type == "client_credentials":
        payload = {'grant_type':oauth_grant_type, 'client_id': oauth_client_id, 'client_secret': oauth_client_secret}

        try:
            r = requests.post(url, headers=headers, json=payload)
            r.raise_for_status()
        except Exception as e:
            print(e)
            exit(1)

        json_response = json.loads(r.content)

        return json.dumps(json_response)


check_config(clearpass_fqdn, oauth_grant_type, oauth_client_id, oauth_client_secret, oauth_username, oauth_password)

clearpass_response = get_access_token(clearpass_fqdn, oauth_grant_type, oauth_client_id, oauth_client_secret, oauth_username, oauth_password)

access_token = clearpass_response['access_token']
token_type = clearpass_response['token_type']
token_expires_in = clearpass_response['expires_in']
scope = clearpass_response['scope']

print(clearpass_response)