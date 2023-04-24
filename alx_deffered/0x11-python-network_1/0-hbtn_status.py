#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 05:14:59 2020
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        content = response.read()
        url = content.decode('utf-8')
        typed = response.info()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(url))
