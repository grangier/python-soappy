#!/usr/bin/env python

import sys
from SOAPpy import SOAP

# Uncomment to see outgoing HTTP headers and SOAP and incoming SOAP.
SOAP.Config.debug = 1

SOAP.Config.BuildWithNoType = 0
SOAP.Config.BuildWithNoNamespacePrefix = 0

if len(sys.argv) > 1 and sys.argv[1] == '-s':
    server = SOAP.SOAPProxy("https://localhost:8080")
else:
    server = SOAP.SOAPProxy("http://admin:pw3340@localhost:8080/",encoding=None)

x = server.sopa()
print x
