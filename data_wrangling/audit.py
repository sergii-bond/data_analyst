#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then
clean it up. In the first exercise we want you to audit the datatypes that can be found in some 
particular fields in the dataset.
The possible types of values can be:
- NoneType if the value is a string "NULL" or an empty string ""
- list, if the value starts with "{"
- int, if the value can be cast to int
- float, if the value can be cast to float, but CANNOT be cast to int.
   For example, '3.23e+07' should be considered a float because it can be cast
   as float but int('3.23e+07') will throw a ValueError
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and a SET of the types
that can be found in the field. e.g.
{"field1: set([float, int, str]),
 "field2: set([str]),
  ....
}

All the data initially is a string, so you have to do some checks on the values first.

"""
import codecs
import csv
import json
import pprint
import re 
import sys

CITIES = 'cities_cut.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal", 
          "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long", 
          "areaLand", "areaMetro", "areaUrban", "postalCode"]

def audit_file(filename, fields):
    fieldtypes = {}

    # YOUR CODE HERE
    with open(filename, 'r') as f:
        r = csv.DictReader(f)
        fieldtypes = {}
        for k in fields:
            fieldtypes[k] = set([])

        for line in r:
            #pprint.pprint(line)
            for k in fields:
                if line[k] == None:
                    fieldtypes[k].add(type(None))
                    continue

                val = line[k].strip()

                if val == "" or val == "NULL":
                    fieldtypes[k].add(type(None))
                    continue

                if re.search(r'^\s*{', val):
                    fieldtypes[k].add(type([]))
                    if k == 'postalCode':
                        print val
                    #print val
                    continue

                try:
                    int(val)
                    fieldtypes[k].add(type(1))
                    #continue
                except:
                    try:
                        float(val)
                        fieldtypes[k].add(type(1.1))
                        #continue
                    except:
                        #if k == 'areaLand':
                        #    print val
                        #fieldtypes[k].add('str')
                        pass



    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])
    
if __name__ == "__main__":
    test()

