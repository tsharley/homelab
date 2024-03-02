#!/usr/bin/env python3
##############################################################################%
import configparser

config = configparser.ConfigParser()
config.read('configs/cf.ini')
my_id = config['account']['id']

print(f"My ID: {my_id}")
