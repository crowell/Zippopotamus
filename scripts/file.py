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
ZIP Directory Helper Function
'''
def zipdir(basedir, archivename):
    assert os.path.isdir(basedir)
    with closing(ZipFile(archivename, "w", ZIP_DEFLATED)) as z:

        # traverse directory recursively 
        for root, dirs, files in os.walk(basedir):
            #ignores empty directories
            for fn in files:
                absfn = os.path.join(root, fn)
                zfn = absfn[len(basedir)+len(os.sep):] #XXX: relative path
                z.write(absfn, zfn)

'''
Picks out all the directories and zips them
'''
def make_zip( countries ):

    print "Zipping folders"

    # for all the country codes
    for cc in countries :
        # make a name for the file
        zipname = cc+".zip"
        directory =  os.path.join(os.getcwd(),cc)
        
        # ZIP all the folders into one
        zipdir(directory,zipname)

        # Print 10 to a line
        count+=1
        sys.stdout.write(cc+" ")
        if not count%10 :
            print ""

    pass   
    

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
    countries = set()
    
    print "Generating Files ... "

    for row in reader :
        
        # If not empty
        if row[0] != '':
            cc = row[0].lower()
            output_dir = os.path.join(os.getcwd(), cc)
            if not os.path.exists(output_dir): os.makedirs(output_dir);
            
            # Print if we have moved onto a new country country
            if cc not in countries:
                countries.add(cc)
                sys.stdout.write(cc+ " ")
                if not len(countries)%10 :
                    print "" 

            postcode = row[1]
            index = dict();

            # Populate information 
            for ii in range(0,len(headers)):
                if 'ignore' not in headers[ii]:
                    index[ headers[ii] ] = unicode(row[ii], 'utf-8');

            raw = json.dumps(index,ensure_ascii=False);
            fout = codecs.open(os.path.join(output_dir,postcode), encoding='utf-8', mode="w+" )
            fout.write( raw )
            fout.close()
    
    make_zip(countries)




main()

