import sys
import os
import csv

from pymongo import Connection
from pymongo.database import Database

appendix_file = '../appendix/country.txt'
header_file = '../appendix/headers.txt'


def remove(csv_file):
    
    # Load Header File 
    with open(header_file, 'rb') as f:
        hfile = csv.reader( f, delimiter=',', quotechar='|')
        headers = hfile.next()
    
    
    # Load Country Appendix
    with  open(appendix_file, 'rb') as f:
        appendix = csv.reader( f,  delimiter=',', quotechar='|') 
        names = dict()
        for lines in appendix:
            if lines[0]!="":
                names[ lines[0] ] = lines[1]

    # Generate N Records
    with open( csv_file , 'rb')  as f:
        reader = csv.reader( f , delimiter=',', quotechar='|') 
        for row in reader:
            record = dict()
            record['country'] = unicode(names[row[0] ], 'utf-8')

            for ii in range(0, len(headers)):
                if 'ignore' not in headers[ii]:
                    record[ headers[ii] ] = unicode( row[ii], 'utf-8' )
            erase(record)

    pass

def erase( record ):
    db['global'].remove(record)

if __name__ == "__main__" :
    
    if ( len(sys.argv) != 4 ):
        print "Usage: %s <username> <password> <csv-files>" % sys.argv[0]

    username = sys.argv[1]
    password = sys.argv[2]
    csv_file = sys.argv[3]
    
    print username
    print password
    print csv_file

    connection = Connection()                   # Replace with mongo-url
    db = Database(connection,'zip')              # Get zip database
    db.authenticate(username,password)           # Authenticate
    
    remove( csv_file )

    


