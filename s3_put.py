#!/usr/bin/python

#-------------------------
#Import required libraries
#-------------------------
import boto
from boto.s3.key import Key
import random


#-------------------------
#Connect to s3 bucket
#-------------------------
s3_connection = boto.connect_s3()
bucket = s3_connection.get_bucket('cheers4beers')
#folder = bucket.list("Tickets")


#-------------------------
#Generate random number to be the filename and ticket number
#-------------------------
ticketNumber = random.randrange(100000,999999)


#-------------------------
#Create file in s3 with the filename of the ticket number
#-------------------------
k = Key(bucket)
k.key = ticketNumber

#-------------------------
#Set the file metadata
#-------------------------
#-------------------------
#Create file in s3 with the filename of the ticket number
#-------------------------
k = Key(bucket)
k.key = ticketNumber

#-------------------------
#Set the file metadata
#-------------------------
k.set_metadata('TicketNumber',ticketNumber)
k.set_metadata('Name','James')
k.set_metadata('Email','jamesstyles@gmail.com')
k.set_metadata('Phone','07788433669')
k.set_metadata('Ticket_Code','c4b2017' + str(ticketNumber))
k.set_metadata('Entry_Count',0)
k.set_metadata('Drinks_Left',0)
k.set_contents_from_string('Test')
print 'Ticket ' + str(ticketNumber) + ' created'
