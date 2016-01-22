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


#-------------------------
#Generate random number to be the filename and ticket number
#-------------------------
ticketNumber = random.randrange(100000,999999)


#-------------------------
#Create file in s3 with the filename and contents of the ticket number
#-------------------------
k = Key(bucket)
k.key = ticketNumber
k.set_contents_from_string('test')
