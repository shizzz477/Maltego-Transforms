#!/usr/bin/python
 
#reverseipdomain.py
#Author: Sudhanshu Chauhan - @Sudhanshu_C
 
#This Script will perform a reverse IP domain check using http://www.yougetsignal.com
#In case yougetsignal is down due to overload, we can also use: http://www.my-ip-neighbors.com/?domain=. Simply change the value of the parameter 'opencnam'.
 
from MaltegoTransform import *
import sys
import urllib2
import re
mt = MaltegoTransform()
mt.parseArguments(sys.argv)
url=mt.getValue()
mt = MaltegoTransform()
opencnam="http://domains.yougetsignal.com/domains.php?remoteAddress="
getrequrl=opencnam+url
header={'User-Agent':'Mozilla',}
req=urllib2.Request(getrequrl,None,header)
response=urllib2.urlopen(req)
domains=re.findall("((?:[0-9]*[a-z][a-z\\.\\d\\-]+)\\.(?:[0-9]*[a-z][a-z\\-]+))(?![\\w\\.])",response.read())
for domain in domains:
  mt.addEntity("maltego.Domain", domain)
mt.returnOutput()
