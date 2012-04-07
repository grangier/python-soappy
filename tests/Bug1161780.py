#!/usr/bin/env python
import sys
sys.path.insert(1, "..")
from SOAPpy.Errors import Error
from SOAPpy.Parser import parseSOAPRPC

original = """<?xml version="1.0"?>
<SOAP-ENV:Envelope
 SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
 xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"
 xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
	<SOAP-ENV:Body>
		<doSingleRecord SOAP-ENC:root="1">
		</doSingleRecord>
	</SOAP-ENV:Body>
	<ErrorString>The CustomerID tag could not be found or the number contained in the tag was invalid</ErrorString></SOAP-ENV:Envelope>

"""

try:
    parseSOAPRPC(original, attrs = 1)
except Error, e:
    if e.msg != "expected nothing, got `ErrorString'":
        raise AssertionError, "Incorrect error message generated: " + e.msg
else:
    raise AssertionError, "Incorrect error message generated"

print "Success"
