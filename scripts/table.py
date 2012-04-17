from __future__ import with_statement
import codecs
import csv
import sys
import json
import os

from contextlib import closing
from zipfile import ZipFile, ZIP_DEFLATED
import os
 
'''
Made specifically for GEONAMES.ORG postal code data parsing
'''
def main():

    if len(sys.argv) <3:
        print "Usage: "+sys.argv[0]+" <csv-file> <country-file>"
        sys.exit(-1)
    
    csvfile = sys.argv[1]
    countryfile = sys.argv[2]

    # get full country names
    cfile = csv.reader( open(countryfile, 'rb' ) , delimiter="\t",quotechar='|')
    names = dict()

    # Map country code to full names
    for lines in cfile:
        if lines[0]!="":
            names[lines[0].lower() ] = lines[1]
    
    # Read the TAB delimited file 
    reader =csv.reader(open(csvfile, 'rb'), delimiter='\t', quotechar='|')
    
    # Keep track of country changes
    min_val = dict()
    max_val = dict()
    total = dict()
    ccodes = set()
    

    print "Generating Files ... "

    for row in reader :
        
        # If not empty
        if row[0] != '':
            
            # Extract the country code
            cc = row[0].lower()
            
            # Post code, NOT APPLICABLE TO FRACE
            postcode = row[1]
            
            # Print if we have moved onto a new country country
            if cc not in ccodes:
                ccodes.add(cc)
                total[cc] = 0
                min_val[cc] = postcode
                max_val[cc] = postcode
            else:
                total[cc]+=1
                max_val[cc] = postcode
    
    # Now I have min/max, ccodes, names and totals for all the countries
    
    html_string = ""
    sorted_codes = sorted( list(ccodes) )

    for cc in sorted_codes:
        
        # Make an information list and fill it
        info = list()
        
        # Country Name
        info.append( names[cc] )
        
        # Country code
        info.append( cc )

        # Min value       
        info.append( url_example( cc , min_val[cc] ) )
        
        # Min to Max range 
        info.append(  min_val[cc]+" : "+max_val[cc] )

        # totals
        info.append( total[cc] )

        html_string += html_row( info )+ "\n"

    print html_string

def url_example( cc, postcode ):
    span_end = "</span>"
    span_red = '<span style="color:darkred;">'
    span_blue = '<span style="color:darkblue;">'
    span_green = '<span style="color:darkgreen;">'

    # Generate Example with colors
    example = ""
    example += span_blue+"zippopotam.us"+span_end+"/"
    example += span_red+cc+span_end+"/"
    example += span_green+postcode+span_end
    
    return example

    
def html_row(info):
    
    end_row = "</tr>"
    start_row = "<tr>"
    
    row = ""
    row += start_row
    for ii in info:
        row +=  "<td>" + str(ii) +"</td>"

    row += end_row

    return row
    




main()

