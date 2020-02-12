import extract_msg
import glob
import os
import re

# Define some variables
path = 'path'
retpath = r'Return-Path: (.*)'
rec = r'Received: (.*)'
recip = r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})'
btc = r'\b[13][a-km-zA-HJ-NP-Z1-9]{25,34}\b'
email = r'\b[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}\b'
email_domain = r'[a-zA-Z0-9._%+-]+@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})'
url = r'[a-zA-Z]+://[-a-zA-Z0-9.]+(?:/[-a-zA-Z0-9+&@#/%=~_|!:,.;]*)?(?:\?[-a-zA-Z0-9+&@#/%=~_|!:,.;]*)?'
domain = r'[a-zA-Z]+://([-a-zA-Z0-9.]+)(?:/[-a-zA-Z0-9+&@#/%=~_|!:,.;]*)?(?:\?[-a-zA-Z0-9+&@#/%=~_|!:,.;]*)?'


# List dedup function
def dedup(x):
  return list(dict.fromkeys(x))

# Loop through messages
f = glob.glob(path + '*.msg')
for filename in f:  

    # Extract desired fields
    msg = extract_msg.Message(filename)
    msg_sender = msg.sender
    msg_to = msg.to
    msg_cc = msg.cc
    msg_date = msg.date
    msg_subj = msg.subject
    msg_head = msg.header
    msg_message = msg.body
    
    # Clean up white space in body
    msg_body = " ".join(msg_message.split())

    # Hunt header data
    head = str(msg_head)

    # Finds the return path
    retm = re.findall(retpath, head)

    # Finds reciept info and hunt IP addresses
    recm = re.findall(rec, head)
    recstr = str(recm)
    recipm = re.findall(recip, recstr)
    rec_ips = dedup(recipm)

    # String message body for search
    body = str(msg_body)

    # Hunt email addresses and dedup
    bodyemail = re.findall(email, body)
    bodyemaild = dedup(bodyemail)
    bodyedom = re.findall(email_domain, body)
    bodyedomd = dedup(bodyedom)

    # Hunt links and domains
    bodyurl = re.findall(url, body)
    bodyurld = dedup(bodyurl)
    bodydom = re.findall(domain, body)
    bodydomd = dedup(bodydom)

    # Hunt BTC Addresses WIP
    bodybtc = re.findall(btc, body)
    
    # Create list of data points
    data = [msg_date, msg_sender, msg_to, msg_cc, msg_subj, body, retm, rec_ips, bodyemaild, bodyurld, bodydomd]

    # Output
    print body

# To do:
# Hunt BTC addresses in body
# Convert data points to data frame???
# Create unique msg id
