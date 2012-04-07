#!/usr/bin/env python

ident = '$Id: SOAPtest.py,v 1.19 2004/04/01 13:25:46 warnes Exp $'

import urllib
import sys
import unittest
import re

sys.path.insert(1, "..")
from SOAPpy import *
config=Config
config.strict_range=1


class SOAPTestCase(unittest.TestCase):
    def testAttributes(self):
        x = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
<soap:Body soap:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<SomeMethod>
<Result>
<Book>
   <title some_attr='some_value'>My Life and Work</title>
</Book>
<Person>
   <name>Henry Ford</name>
   <age> 49 </age>
   <height> 5.5 </height>
</Person>
</Result>
</SomeMethod>
</soap:Body>
</soap:Envelope>
'''
        # parse rules
        y = parseSOAPRPC(x)
        self.assertEquals(y.Result.Book.title._attrs[(None, 'some_attr')], 'some_value');

if __name__ == '__main__':
    unittest.main()
