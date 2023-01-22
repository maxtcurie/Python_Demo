#get from https://stackoverflow.com/questions/54785152/replace-tab-with-space-in-entire-text-file-python/54785524
inputFile = open('./Input/Tab_replace_test_file.py', 'r') 
exportFile = open('./Output/Tab_replace_test_file_copy.py', 'w')
for line in inputFile:
   new_line = line.replace('\t', '    ')
   exportFile.write(new_line) 

inputFile.close()
exportFile.close()

#method2
def replace(inputFile,exportFile,target,replacement):
   inputFile = open(inputFile, 'r') 
   lines_original=inputFile.readlines()
   inputFile.close()
   
   exportFile = open(exportFile, 'w')
   for line in lines_original:
      new_line = line.replace(target, replacement)
      exportFile.write(new_line) 
   exportFile.close()
replace('./Input/Tab_replace_test_file_2.py',\
         './Output/Tab_replace_test_file_2.py',\
         '\t','    ')