# output only those credit card numbers which have two or more 
# consecutive occurences of the same digit (which may be separated by a space
cat | grep -P '(\d)\s?\1'