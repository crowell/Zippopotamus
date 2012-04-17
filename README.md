# Zippopotamus API

The free open source static API for all the worlds postal codes.

See [zippopotam.us](http://zippopotam.us) for how to use the API.

## To Contribute Changes:

Postal codes change a lot! And keeping track is tough. Here is how you can help

Please correct any mistakes or add any new countries that we are missing by editing

`raw/allCountries.txt` : Tab Delimited Dump of All Countries Postal Codes from [geonames.org](http://www.geonames.org) 

If adding a new country, you need to add a new line to:

`raw/country.txt` : Tab Delimited file, 2-Letter ISO Country code and Country Name

#### Formatting 
The data format is tab-delimited text in utf8 encoding, with the following fields :

- `country code`      : iso country code, 2 characters
- `postal code`       : varchar(20)
- `place name`        : varchar(180)
- `admin name1`       : 1. order subdivision (state) varchar(100)
- `admin code1`       : 1. order subdivision (state) varchar(20)
- `admin name2`       : 2. order subdivision (county/province) varchar(100), **Ignored API**
- `admin code2`       : 2. order subdivision (county/province) varchar(20), **Ignored by API**
- `admin name3`       : 3. order subdivision (community) varchar(100), **Ignored by API**
- `admin code3`       : 3. order subdivision (community) varchar(20), **Ignored by API**
- `latitude`          : estimated latitude (wgs84)
- `longitude`         : estimated longitude (wgs84)
- `accuracy`          : accuracy of lat/lng from 1=estimated to 6=centroid **Ignored by API**

## Exceptions and Caveats:

- `gb` Great Britain : Only supports 'in-codes' no 'out-codes' supported
- `fr` France : CEDEX is supported in the JSON response, queries are only 5 digit numbers
- `ar` Argentina : Only the 4 digit old version is supported at the moment
- `br` Brazil : Only major postal codes are available (Codes ending with -000 and the major code per municipality)
- `sk` Slovak Rep. : Please note that there is a space in the postal code

## Questions?

Submit an issue or contact [Jeff](http://twitter.com/jeffreycrowell) or [Samir](http://twitter.com/samirahmed_27)

&copy; Jeff Crowell - Samir Ahmed 2012