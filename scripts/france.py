from __future__ import with_statement
import codecs
import csv
import sys
import json
import os

import os


   

'''
Made specifically for GEONAMES.ORG postal code data parsing
'''
def main():

    if len(sys.argv) <3:
        print "Usage: "+sys.argv[0]+" <csv-file> <header-file>"
        sys.exit(-1)
    
    headerfile = sys.argv[2]
    csvfile = sys.argv[1]

    # get the headers, COMMA delimited 
    hfile = csv.reader( open(headerfile, 'rb'), delimiter=',', quotechar='|' )
    headers = hfile.next()

    # Print list of valid header terms
    print filter( lambda hh: "ignore" not in hh , headers )

    # Read the TAB delimited file 
    reader =csv.reader(open(csvfile, 'rb'), delimiter='\t', quotechar='|')
    
    # Keep track of country changes
    
    print "Generating Files for France "

    for row in reader :
        
        # If only france
        if row[0].lower() == 'fr':
            cc = row[0].lower()
            output_dir = os.path.join(os.getcwd(), cc)
            if not os.path.exists(output_dir): os.makedirs(output_dir);
           
            
            postcode = row[1].split(' ')[0]
            index = dict();

            # Populate information 
            for ii in range(0,len(headers)):
                if 'ignore' not in headers[ii]:
                    index[ headers[ii] ] = unicode(row[ii], 'utf-8');

            raw = json.dumps(index,ensure_ascii=False);
            fout = codecs.open(os.path.join(output_dir,postcode), encoding='utf-8', mode="w+" )
            fout.write( raw )
            fout.close()
    




main()

