#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "BJS Engineering Team"
__copyright__ = "Copyright 2020, BJS Home Delivery"
__credits__ = ["Rana Ramnik singh", "Callam Delaney", "Jeevan Kumar"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Anish Kumar Dhanka"
__email__ = "anish@bjshomedelivery.com"

"""Dnsmeapi 
   simplify dnsmadeeasy api calls for https://api-docs.dnsmadeeasy.com/?version=latest#6a7eef29-27fb-4f37-af89-e3ec4a3dcf66
"""

import requests
import hmac
import hashlib
from email.utils import formatdate


class Dnsmeapi:
    hmac = None
    request_date = None
    api_key = ""
    api_secret_key = ""

    def __init__(self, api_key, api_secret_key):
        self.api_key = api_key
        self.api_secret_key = api_secret_key

    def make_request(self, method_type, url, payload):
        self.request_date = formatdate(timeval=None, localtime=False, usegmt=True)
        try:
            self.hmac = hmac.new(
                bytes(self.api_secret_key, "UTF-8"),
                bytes(self.request_date, "UTF-8"),
                hashlib.sha1,
            ).hexdigest()
        except Exception as e:
            raise e

        headers = {
            "Content-Type": "application/json",
            "x-dnsme-hmac": self.hmac,
            "x-dnsme-apiKey": self.api_key,
            "x-dnsme-requestDate": self.request_date,
        }

        try:
            response = requests.request(method_type, url, headers=headers, data=payload)
            return response.text.encode('utf-8')
        except Exception as e:
            raise e
