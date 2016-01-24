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
Name=key.get_metadata('name')
print Name
