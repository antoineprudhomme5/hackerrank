# print first column of lines that hasn't 4 columns
cat | awk '(NF != 4){print "Not all scores are available for " $1}'