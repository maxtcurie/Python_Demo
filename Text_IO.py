
f=open("demo_text.txt","r")  #name of the file "demo_text.txt",    "r" ==> read the text
f1=open("demo_text.txt","r")


#For reading the line and lines
#https://www.w3schools.com/python/ref_file_readline.asp
line0=f.readline()   #read one line
print(line0)
print(line0[:-1])
line1=f.readline()   #read the next line
print(line1)
line2=f.readline()
print(line2)
line3=f.readline()
print(line3)

print("*******************")

lines=f1.readlines() #read multiple lines
print(str(lines))

print("*******************")
for line in lines:
    print(line.split(',')) 


# for string split
# https://www.geeksforgeeks.org/python-string-split/
print("*******************")

text = 'geeks for geeks'

# Splits at space 
print(text.split()) 

word = 'geeks, for, geeks'

# Splits at ',' 
print(word.split(',')) 

word = 'geeks:for:geeks'

# Splitting at ':' 
print(word.split(':')) 

word = 'CatBatSatFatOr'

# Splitting at 3 
print([word[i:i+3] for i in range(0, len(word), 3)]) 


print("*******************")
file=open("demo_text.txt","w")
file.write(line0)
file.write(line1)
file.write(line2)
file.write(line3)



txt = "     banana     "
x = txt.strip()
print(x)

y=float('          1.0000000000')
print(y)

'''
#From https://stackabuse.com/writing-to-a-file-with-pythons-print-function/
original_stdout = sys.stdout # Save a reference to the original standard output
with open('output.txt', 'w') as f:
	sys.stdout = f # Change the standard output to the file we created.
	#From: https://stackoverflow.com/questions/19124601/pretty-print-an-entire-pandas-series-dataframe
	with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
		print(properties)
	sys.stdout = original_stdout # Reset the standard output to its original value
'''
