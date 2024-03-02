#!/usr/bin/env python3
##############################################################################%
import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {}
config['account'] = {
    'id': '55a2f70f72deb9f44df3a1cdfbb6c44f',
}
config['api'] = {
    'global_key': '46162a0443209809053f72ef5d04ba78695cd',
    'origin_ca_key': 'v1.0-68679d50becd81d3edc6bd19-f1fdef49064b29a4c383d38f3d0b14c800fad458dc2935c95c593e475041f668bffce58ca22eee2387f5fa47a77e18f3d746d824693e4aab480d516fd4964deef2ca2829d149fce94a',
    'token': 'TkRZrVEXybVv6Le8u8xNipM2OOZBy4ybf84Hk0be',
    'token_ZoneDNSEdit': 'EI1QHA6pth57OL5Mk7b0B7zI6a_MdBWxlv9CJTRW',
    'token_admin_all': '2EZLYuZpavnVQxXhFwuFN3rCHOCNMaN7RnrZC5RG'
}
config['zone'] = {
    'id': '6505c5814c346022bbf06fb07179d3a0',
}

with open('configs/cf.ini', 'w') as configfile:
    config.write(configfile)
