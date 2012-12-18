#!usr/bin/env/python
#
#
#
##*****************************************************************************************##
## Python_Practical_Parser.py
## This program was created to satisfy the 'coding practical' portion of
## the requirements of Cloudspace's process.
#
#
## The program is designed to take a raw email .txt file, and parse it for
## relavent data. 
#
## The time spent coding was kept to a 60 minute interval, to keep with the application
##  page's recommendation 
#
## Often, in my current industry, I've needed to take the header details of emails
## and put them into respective fields in a database. Therefore, the relavent data
## will consist of the To, From, Subject and Date of the email.
#
#
## Original Author: Joshua Bush
#
#
## Dec. 17th, 2012 - Rev. 0
## ****************************************************************************************##


import sys
import re  # Regular expressions just seem to be the easiest way to quickly and effectively 
            # get the job done.
        

## According to RFC2822 header fields are lines composed of a field name, followed by a colon
## followed by a field body, and terminated by CRLF. 
## The field name MUST be composed of US-ASCII characters, and the colon.
## This will make it easy to search for common fields, such as the "To" and the "From", etc.,

def Parse_Email():
    Header_Data = []
    ToScan= re.compile(r'To: [\w\s]+?<([\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4})>') 
    #It is important to note that this only grabs the first email
    #address. I should extend it to cover more (; seperated) in the future.
    FromScan= re.compile(r'From: [\w\s]+?<([\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4})>')
    DateScan = re.compile(r'Date: (.*)')
    SubjectScan= re.compile(r'Subject: (.*)')
    #
    # To clarify the above: A pattern is compiled for each regular expression to be matched.
    # To dissect the regular expressions a bit, the "To:" simply tries to match that string
    # The [\w\s]+? will match one or more consecutive characters or spaces
    # A '\-' just escapes a hyphen to include it in the regex, and \. matches periods.
    # The @ and the <> match their respective literals. 
    # The [a-zA-Z]{1.4} at the end of the expression is matching between 1 and 4 lower or uppercase letters (e.g., 'com')
    #
    for line in open("email.txt"):
        Header_Data.extend([m.group(1) for m in DateScan.finditer(line)])    # By storing group(1), only the data in the field after the 
        Header_Data.extend([m.group(1) for m in SubjectScan.finditer(line)]) # header label will be stored.       
        Header_Data.extend([m.group(1) for m in FromScan.finditer(line)])
        Header_Data.extend([m.group(1) for m in ToScan.finditer(line)])
                # The results are stored in the Header_Data list for quick reference and assignment.
    print Header_Data
    #May be useful to return the data parsed, for now, the output should suffice.

Parse_Email()
