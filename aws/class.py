#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import subprocess
import smtplib


yesstartime = datetime.datetime.now() - datetime.timedelta(days=1)
yesendtime = datetime.datetime.now()
enddate = yesendtime.strftime("%Y-%m-%d")
stardate = yesstartime.strftime("%Y-%m-%d")

TolPeakVV = 39247
#mailme(stardate,TolPeakVV);
subject = "The peak VV yesterday, (%s) is %s" % (stardate,TolPeakVV)
#headers = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" % (sender,to,subject)
#msg = headers + "The peak VV yesterday (" + stardate + ") is " + TolPeakVV
#test
print subject
#snapshot test
#test no fast forward
#test local git