# importing panda library 
import pandas as pd 
import csv
#input file
fin = open("test.txt", "rt")
#output file to write the result to
fout = open("out_test.txt", "wt")
#for each line in the input file
for line in fin:
	#read replace the string and write to output file
	fout.write(line.replace(')', '\n').replace(', (', ' ').replace('[(',' ').replace(']',''))
	
#close input and output files
fin.close()
fout.close()
dataframe1 = pd.read_csv("out_test.txt",delimiter=',')
dataframe1.to_csv('test.csv',index = None)
