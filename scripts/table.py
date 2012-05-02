from pymongo import Connection
from pymongo.database import Database
import sys
import json
import sys
import os

 
'''
Generates Table and Information from MONGODB
'''
def build_table():
    
    
    # Keep track of country changes
    min_val = dict()
    names = dict()
    max_val = dict()
    total = dict()
    ccodes = set()
    
    print "Generating Files ... "

    for record in list(db['global'].find()) :
        
        # If not empty
        if record['country abbreviation'] != '':
            
            # Extract the country code
            cc = record['country abbreviation']
            
            # Print if we have moved onto a new country country
            if cc not in ccodes:
                print cc
                ccodes.add(cc)
                names[cc] = record['country']
                total[cc] = 1
                min_val[cc] = record['post code']
                max_val[cc] = record['post code']
            else:
                if max_val[cc] < record['post code']:
                    max_val[cc] = record['post code']
                if min_val[cc] > record['post code']:
                    min_val[cc] = record['post code']
                total[cc]+=1
    
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
    



if __name__ == "__main__":

    if ( len(sys.argv) != 2 ):
        print "Usage: %s <username> <password>" % sys.argv[0]

    username = sys.argv[1]
    password = sys.argv[2]
    
    print username
    print password

    connection = Connection()              # Specific url
    db = Database(connection,'zip')     # Get zip database
    db.authenticate(username,password)  # Authenticate
    
    build_table();


