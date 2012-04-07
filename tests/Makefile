PYTHON=python

default: echoClient echoHeader largeDataTest bugs \
	 card independent \
         testClient1 outside_services

bugs: Bug1001646 Bug916265 Bug1161780 Bug1936883

echoClient: 
	$(PYTHON) echoServer.py >& echoServer_echoClient.log &
	sleep 5s # wait for server to start up
	$(PYTHON) echoClient.py

echoHeader:
	$(PYTHON) echoServer.py >& echoServer_echoHeader.log &
	sleep 5s # wait for server to start up
	$(PYTHON) echoHeader.py

largeDataTest:
	$(PYTHON) echoServer.py >& echoServer_largeDataTest.log &
	sleep 5s # wait for server to start up
	$(PYTHON) largeDataTest.py

card:
	$(PYTHON) cardServer.py >& cardServer.log &
	sleep 5s # wait for server to start up
	$(PYTHON) cardClient.py

esj:
	$(PYTHON) esj_test_server.py >& esj_test.log &
	$(PYTHON) esj_test_client.py


Bug1936883:
	$(PYTHON) Bug1936883.py

Bug1161780:
	$(PYTHON) Bug1161780.py

Bug1001646:
	$(PYTHON) echoServer.py >& echoServer_largeDataTest.log &
	sleep 5s # wait for server to start up
	$(PYTHON) Bug1001646.py

Bug916265:
	$(PYTHON) echoServer.py >& echoServer_Bug916265.log &
	sleep 5s # wait for server to start up
	$(PYTHON) Bug916265.py

outside_services:
	$(PYTHON) alanbushTest.py
	$(PYTHON) BabelfishWSDLTest.py
	$(PYTHON) GoogleTest.py
	$(PYTHON) quoteTest.py
	$(PYTHON) simpleWSDL.py
	$(PYTHON) testWSDL.py

independent:
	$(PYTHON) speedTest.py
	$(PYTHON) Bug918216.py
	-$(PYTHON) ComplexTypes.py
	-$(PYTHON) SOAPtest.py # one subtest will fail
	$(PYTHON) TCtest.py
	$(PYTHON) testleak.py
	-$(PYTHON) translateTest.py
	-$(PYTHON) weatherTest.py
	-$(PYTHON) whoisTest.py
	-$(PYTHON) xmethods.py
	$(PYTHON) ZeroLengthArray.py

testClient1:
	$(PYTHON) testClient1.py

broken:
	$(PYTHON) newsTest.py
	$(PYTHON) excelTest.py
	$(PYTHON) storageTest.py
