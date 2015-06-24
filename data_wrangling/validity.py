"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in range, as described above,
  write that line to the output_good file
- if the value of the field is not a valid year, 
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the 
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import pprint
from zipfile import ZipFile
import re

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def process_file(input_file, output_good, output_bad):

    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        #pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(header)

        regexp = re.compile(r'dbpedia.org')

        #COMPLETE THIS FUNCTION

        f_good = open(output_good, "w")
        writer_good = csv.DictWriter(f_good, delimiter=",", fieldnames= header)
        writer_good.writeheader()

        f_bad = open(output_bad, "w")
        writer_bad = csv.DictWriter(f_bad, delimiter=",", fieldnames= header)
        writer_bad.writeheader()

        for line in reader:
            if re.search(regexp, line["URI"]):
                good = 0
                year = line["productionStartYear"]
                match = re.search(r'^\s*(\d+)\s*-', year)

                if match != None:
                    year = int(match.group(1))

                    if year >= 1886 and year <= 2014:
                        line["productionStartYear"] = year
                        good = 1

                if good == 1:
                    writer_good.writerow(line)
                    #print(year)
                else:
                    #print(year)
                    writer_bad.writerow(line)
                #for key, value in line.iteritems():
                #        print key

        f_good.close()
        f_bad.close()



def open_zip(datadir):
    with ZipFile('{0}.zip'.format(datadir), 'r') as myzip:
        myzip.extractall()


def test():

    open_zip(INPUT_FILE) 
    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()
