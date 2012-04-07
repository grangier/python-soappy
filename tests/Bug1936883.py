#!/usr/bin/env python

ident = '$Id: speedTest.py 243 2003-05-21 14:52:37Z warnes $'

import time
import sys
sys.path.insert(1, "..")

from SOAPpy import parseSOAP, parseSOAPRPC

env = '''<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsd="http://www.w3.org/1999/XMLSchema" xmlns:xsd2="http://www.w3.org/2000/10/XMLSchema" xmlns:xsd3="http://www.w3.org/2001/XMLSchema" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/1999/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/">
%s
</SOAP-ENV:Envelope>'''

xml = env % '''<SOAP-ENV:Body>
<_1 SOAP-ENC:arrayType="xsd:int[4]" SOAP-ENC:offset="[2]" xsi:type="SOAP-ENC:Array">
    <_2 SOAP-ENC:arrayType="xsd:int[2]" xsi:type="SOAP-ENC:Array">
        <item>1</item>
        <item>2</item>
    </_2>
    <_3 SOAP-ENC:arrayType="xsd:double[2]" xsi:type="SOAP-ENC:Array">
        <item>3.3</item>
        <item>4.4</item>
    </_3>
    <_4 SOAP-ENC:arrayType="xsd:bool[2]" xsi:type="SOAP-ENC:Array">
        <item>0</item>
        <item>1</item>
    </_4> 
    <_5 SOAP-ENC:arrayType="xsd:bool[2]" xsi:type="SOAP-ENC:Array">
        <item>False</item>
        <item>True</item>
    </_5> 
</_1>
</SOAP-ENV:Body>'''


x = parseSOAPRPC(xml)


assert( x[2] == [ 1, 2 ] )
assert( x[3] == [ 3.3, 4.4 ] )

# These previously failed, instead having strings
assert( x[4] == [ False, True ] )
assert( x[5] == [ False, True ] )

print "Success"

