
# clearpass-api-auth

![version 2017.02](https://img.shields.io/badge/Version-2017.02-brightgreen.svg "version 2017.02") [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) ![Aruba Security Group](https://img.shields.io/badge/Source-Aruba_Security-orange.svg "Aruba Security Group")


## Overview
This is a Python3 code snippet for obtaining an OAuth 2.0 access token for accessing the ClearPass REST API.

## Current Version
2017.02 (2017-10-07)

## Change Log
### 2017.02 (2017-10-07)
Parsed out access_token, token_type, token_expires_in, and scope
### 2017.01 (2017-07-28)
Initial Release

## Pre-requisites
* An API client must be defined in ClearPass Guest under Administration » API Services » API Clients
* An authentication service must be created in ClearPass Policy Manager to handle the OAuth 2.0 request

## Usage
Configure the required parameters in config/params.cfg:
* clearpass_fqdn 
* grant_type

The remaining parameters vary by grant type.

Call the script with no arguments: 

> `python3 clearpassauth.py`

## License
Copyright (c) Hewlett Packard Enterprise Development LP. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License").

## Other Information
Author: @timcappalli, Aruba Security Group

Organization: Aruba, a Hewlett Packard Enterprise company
