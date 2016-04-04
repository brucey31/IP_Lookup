__author__ = 'brucepannaman'
import csv
import urllib
import re
import json

# This script takes a csv file of ip addresses and creates a new file with their locations as the second field

ifile = open('/Users/Bruce/Desktop/IP_Lookup_test.csv', "rb")
reader = csv.reader(ifile, dialect=csv.excel_tab)

new_rows_list = []
x = 0

for rows in reader:
    # Save header row.
    # print rows[0]
    # print urllib.urlopen('http://api.hostip.info/get_html.php?ip=%s&position=true' % rows[0]).read()
    new_row = [rows[0],
               re.findall('name":(.*),"code',
                          urllib.urlopen('http://geoip.nekudo.com/api/%s/en/short' % rows[0]).read(), re.M | re.I)]

    if x % 5 == 0:
        print 'Looked up ' + str(x) + ' IP addresses so far'
    new_rows_list.append(new_row)

    x += 1

print new_rows_list
ifile.close()



# Do the writing
file2 = open('/Users/Bruce/Desktop/IP_Lookup_test_results.csv', 'wb')
writer = csv.writer(file2)
writer.writerows(new_rows_list)
file2.close()
