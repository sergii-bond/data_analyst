#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then clean it up.

Since in the previous quiz you made a decision on which value to keep for the "areaLand" field,
you now know what has to be done.

Finish the function fix_area(). It will receive a string as an input, and it has to return a float
representing the value of the area or None.
You have to change the function fix_area. You can use extra functions if you like, but changes to process_file
will not be taken into account.
The rest of the code is just an example on how this function can be used.
"""
import codecs
import csv
import json
import pprint
import re

CITIES = 'cities_cut.csv'


def fix_area(area):

    # YOUR CODE HERE
    area = area.strip()

    if area == "" or area == "NULL" or area == None:
        return None

    try:
        area = int(area)
        return area 
    except:
        try:
            area = float(area)
            return area 
        except:
            pass

    match = re.search(r'^\s*{(.*)\|(.*)}\s*$', area)

    if match:
        #print area
        #print match.group(1)
        #print match.group(2)
        f1 = float(match.group(1))
        f2 = float(match.group(2))
        m1 = re.search(r'\d+\.(\d+)e', match.group(1))
        m2 = re.search(r'\d+\.(\d+)e', match.group(2))

        if int(m1.group(1)) > int(m2.group(1)):
            area = f1
        else:
            area = f2

        return area

    return None


def process_file(filename):
    # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        #skipping the extra metadata
        for i in range(3):
            l = reader.next()

        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "areaLand" in line:
                line["areaLand"] = fix_area(line["areaLand"])
            data.append(line)

    return data


def test():
    data = process_file(CITIES)

    print "Printing three example results:"
    for n in range(5,8):
        pprint.pprint(data[n]["areaLand"])
    #print data[8]["areaLand"] 
    assert data[3]["areaLand"] == None        
    assert data[8]["areaLand"] == 55166700.0
    assert data[20]["areaLand"] == 14581600.0
    assert data[33]["areaLand"] == 20564500.0    


if __name__ == "__main__":
    test()
