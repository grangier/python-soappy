Summary:       SOAPpy
Name:          SOAPpy
Version:       0.9.7
Release:       2
License:       Copyright (c) 2001, Cayce Ullman.
Group:         Productivity/Networking/Web/Applications
Source:        SOAPpy-%{version}.tgz
Requires:      python >= 2.2
BuildArch:     noarch
AutoReq:       no
Packager:      Antonio Beamud Montero <antonio.beamud@wanadoo.es>

%description
SOAP implementation by Cayce Ullman and Brian Matthews.
%prep 
%setup SOAPpy-%{version}

%build

%install
mkdir -p /usr/share/doc/SOAPpy/bid
cp -a bid/* /usr/share/doc/SOAPpy/bid
mkdir -p /usr/share/doc/SOAPpy/tests
cp -a tests/* /usr/share/doc/SOAPpy/tests
cp -a TCtest.py /usr/share/doc/SOAPpy/tests
mkdir -p /usr/share/doc/SOAPpy/contrib
cp contrib/* /usr/share/doc/SOAPpy/contrib/
cp docs/* /usr/share/doc/SOAPpy/
mkdir -p /usr/share/doc/SOAPpy/tools
cp -a tools/* /usr/share/doc/SOAPpy/tools
cp README /usr/share/doc/SOAPpy/
cp echoServer.py /usr/share/doc/SOAPpy/
cp speedTest.py /usr/share/doc/SOAPpy/
cp CHANGELOG /usr/share/doc/SOAPpy/
cp SOAPtest.py /usr/share/doc/SOAPpy/tests
cp excelTest.py /usr/share/doc/SOAPpy/
cp echoClient.py /usr/share/doc/SOAPpy/
mkdir -p /usr/share/doc/SOAPpy/validate
cp -a validate/* /usr/share/doc/SOAPpy/validate
cp SOAP.py /usr/lib/python/site-packages/

%clean

%pre

%post

%preun

%postun

%files
%defattr(-,root,root)
/usr/share/doc/SOAPpy/bid/monitorClient.py
/usr/share/doc/SOAPpy/bid/inventoryServer.py
/usr/share/doc/SOAPpy/bid/inventory.servers
/usr/share/doc/SOAPpy/bid/inventoryClient.py
/usr/share/doc/SOAPpy/tests/TCtest.py
/usr/share/doc/SOAPpy/simpleTypes.txt
/usr/share/doc/SOAPpy/attrs.txt
/usr/share/doc/SOAPpy/quickstart.txt
/usr/share/doc/SOAPpy/complexTypes.txt
/usr/share/doc/SOAPpy/contrib/soap_cli.py
/usr/share/doc/SOAPpy/contrib/soap_handler.py
/usr/share/doc/SOAPpy/tests/cardServer.py
/usr/share/doc/SOAPpy/tests/guidTest.py
/usr/share/doc/SOAPpy/tests/alanbushTest.py
/usr/share/doc/SOAPpy/tests/newsTest.py
/usr/share/doc/SOAPpy/tests/weatherTest.py
/usr/share/doc/SOAPpy/tests/fortuneTest.py
/usr/share/doc/SOAPpy/tests/cardClient.py
/usr/share/doc/SOAPpy/tests/quoteTest.py
/usr/share/doc/SOAPpy/tests/storageTest.py
/usr/share/doc/SOAPpy/tests/wordFindTest.py
/usr/share/doc/SOAPpy/tests/itimeTest.py
/usr/share/doc/SOAPpy/tests/whoisTest.py
/usr/share/doc/SOAPpy/tests/translateTest.py
/usr/share/doc/SOAPpy/tools/interop2html.py
/usr/share/doc/SOAPpy/README
/usr/share/doc/SOAPpy/echoServer.py
/usr/share/doc/SOAPpy/speedTest.py
/usr/share/doc/SOAPpy/CHANGELOG
/usr/share/doc/SOAPpy/tests/SOAPtest.py
/usr/share/doc/SOAPpy/excelTest.py
/usr/share/doc/SOAPpy/echoClient.py
/usr/share/doc/SOAPpy/validate/silab.servers
/usr/share/doc/SOAPpy/validate/silabserver.py
/usr/share/doc/SOAPpy/validate/server.pem
/usr/share/doc/SOAPpy/validate/silabclient.py
/usr/share/doc/SOAPpy/validate/soapware.py
/usr/lib/python2.2/site-packages/SOAP.py