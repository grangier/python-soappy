#!/usr/bin/env python

ident = '$Id: speedTest.py 243 2003-05-21 14:52:37Z warnes $'

import time
import sys
from SOAPpy import fpconst
sys.path.insert(1, "..")

from SOAPpy import parseSOAP, parseSOAPRPC

env = '''<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsd="http://www.w3.org/1999/XMLSchema" xmlns:xsd2="http://www.w3.org/2000/10/XMLSchema" xmlns:xsd3="http://www.w3.org/2001/XMLSchema" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/1999/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/">
%s
</SOAP-ENV:Envelope>'''

xml = env % '''<SOAP-ENV:Body>
<result>
  <_1 SOAP-ENC:arrayType="xsd:double[2]" xsi:type="SOAP-ENC:Array">
    <item>3.3</item>
    <item>4.4</item>
    <item>NaN</item>
    <item>Inf</item>
    <item>+Inf</item>    
    <item>Infinity</item>
    <item>+Infinity</item>        
    <item>-Inf</item>
    <item>-Infinity</item>
  </_1>
</result>
</SOAP-ENV:Body>'''


x = parseSOAPRPC(xml)['_1']

assert( x[0:2] == [ 3.3, 4.4 ] )
assert( fpconst.isNaN(    x[2] ) )
assert( fpconst.isPosInf( x[3] ) )
assert( fpconst.isPosInf( x[4] ) )
assert( fpconst.isPosInf( x[5] ) )
assert( fpconst.isPosInf( x[6] ) )
assert( fpconst.isNegInf( x[7] ) )
assert( fpconst.isNegInf( x[8] ) )

print "Success"

