"""
config.py
Author: [Your Name]
Date: [Current Date]
Description: Configuration for the OKX client and global settings.
Iteration: init code
"""

from okx_api import OKXClient

API_KEY = "58dcc0cb-9d9c-4cf4-aa98-60463b177723"
SECRET_KEY = "24029CDB01E860A0B4AED063F23B5421"
PASSPHRASE = "Qwe133656769!"

okx_client = OKXClient(API_KEY, SECRET_KEY, PASSPHRASE)
