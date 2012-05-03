# Zippopotamus API

The free open source static API for all the worlds postal codes.

See [zippopotam.us](http://www.zippopotam.us) for how to use the API.

## To Contribute Changes:

Postal codes change a lot! And keeping track is tough. Here is how you can help

Please correct any mistakes or add any new countries that we are missing by adding a new file in the`raw/` folder

This is a csv file with `"` quotations around each term.

A sample file is included in `raw/sample.txt` which shows how to add records for the imaginery country of Atlantis,


#### Formatting 
The data format is tab-delimited text in utf8 encoding, with the following fields :

- `country`             : This is the country's name, like 'Spain'
- `country abbreviation': This is the ISO 2 letter country code like, "ES" for Spain 
- `post code`           : This is the postal/zip code of the area, '90210'
- `place name`          : This is a town/city/metro name like 'San Francisco'
- `state`               : This is a state or province or region name like 'California'
- `state abbreviation`  : This is a state abbreviation, like 'CA'
- `latitude`          : estimated latitude 
- `longitude`         : estimated longitude

## Exceptions and Caveats:

- `gb` Great Britain : Only supports 'in-codes' no 'out-codes' supported
- `fr` France : CEDEX is supported in the JSON response, queries are only 5 digit numbers
- `ar` Argentina : Only the 4 digit old version is supported at the moment
- `br` Brazil : Only major postal codes are available (Codes ending with -000 and the major code per municipality)
- `sk` Slovak Rep. : Please note that there is a space in the postal code

## Questions?

Submit an issue or contact [Jeff](http://twitter.com/jeffreycrowell) or [Samir](http://twitter.com/samirahmed_27)

&copy; Jeff Crowell - Samir Ahmed 2012