#!/usr/bin/python

#-------------------------
#Import required libraries
#-------------------------
import boto
from boto.s3.key import Key
import random
import sys

#-------------------------
#Connect to s3 bucket
#-------------------------
s3_connection = boto.connect_s3()
bucket = s3_connection.get_bucket('cheers4beers')
#folder = bucket.list("Tickets")

FileName = sys.argv[1]
print FileName
key = bucket.get_key(FileName)
TicketNumber=key.get_metadata('ticketnumber')
Name=key.get_metadata('name')
Email=key.get_metadata('email')
Phone=key.get_metadata('phone')
TicketCode=key.get_metadata('ticket_code')
EntryCount=key.get_metadata('entry_count')
DrinksLeft=key.get_metadata('drinks_left')


#-------------------------
#Check whether the ticket has already been scanned
#Return scan status and increment scan count
#-------------------------

EntryCount = int(EntryCount)
print EntryCount

if EntryCount == 0:
   print 'Welcome in ' + Name + '!'
else:
   print 'Already scanned ' + str(EntryCount) + ' times!'

print Name

OldEntryCount = int(EntryCount)
NewEntryCount = OldEntryCount + 1

#-------------------------
#Re-create file in s3 with the filename of the ticket number
#-------------------------
k = Key(bucket)
k.key = TicketNumber

#-------------------------
#Set the file metadata
#-------------------------
k.set_metadata('TicketNumber',TicketNumber)
k.set_metadata('Name',Name)
k.set_metadata('Email',Email)
k.set_metadata('Phone',Phone)
k.set_metadata('Ticket_Code',TicketCode)
k.set_metadata('Entry_Count',NewEntryCount)
k.set_metadata('Drinks_Left',DrinksLeft)
k.set_contents_from_string('Test')
print 'Ticket ' + str(TicketNumber) + ' recreated'
