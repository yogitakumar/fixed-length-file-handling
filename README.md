# fixed-length-file-handling

This program take fixed length file as input and extract 4:7 char and 11,12 char from file and write it to second file (ignoring header and trailer record)

for example: 

 python fixed_length_field_extraction.py './test/fixed_length.txt' './test/output_file.txt'
 
 input file:
 
Header
0001GBP2000CR
0001GBP1000DR
0002USD0500DR
0002USD1500CR
Trailer
