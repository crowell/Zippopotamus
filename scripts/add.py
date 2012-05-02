import sys
import os
import csv

from pymongo import Connection
from pymongo.database import Database

appendix_file = '../appendix/country.txt'
header_file = '../appendix/headers.txt'


def add(csv_file):
    
    # Generate N Records
    with open( csv_file , 'rb')  as f:
        reader = csv.reader( f , delimiter=',', quotechar='"') 
        headers = reader.next()
        for row in reader:
            record = dict()

            for ii in range(0, len(headers)):
                if 'ignore' not in headers[ii]:
                    record[ headers[ii] ] = unicode( row[ii], 'utf-8' )
            save(record)

    pass

def save( record ):
    db['global'].save(record)

if __name__ == "__main__" :
    
    if ( len(sys.argv) != 5 ):
        print "Usage: %s <username> <password> <url> <csv-files>" % sys.argv[0]

    username = sys.argv[1]
    password = sys.argv[2]
    url  =     sys.argv[3]
    file_list = sys.argv[4:]
    
    print username
    print password
    print len(file_list)

    if ( len(url) == 0 ):
        connection = Connection()              # Connect to localhost
    else:
        connection = Connection( url )         # Connect to remote db
        
    db = Database(connection,'zip')              # Get zip database
    db.authenticate(username,password)           # Authenticate
    

    for csv_file in file_list:  # Add all the files 
        add( csv_file )

    


