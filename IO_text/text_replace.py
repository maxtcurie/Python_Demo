import os

#from: https://www.gnu.org/software/sed/manual/html_node/Command_002dLine-Options.html
#sed OPTIONS... [SCRIPT] [INPUTFILE...]

#replace a to b in the whole file
os.system('sed -i -e "s/a/b/g" test_text.txt ')