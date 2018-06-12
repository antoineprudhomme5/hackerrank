# first column => student ID
# 2th, 3th, 4th => student notes
# check if the student passed or failed
cat | awk '{
    if ($2 >= 50 && $3 >= 50 && $4 >= 50)
        print $1 " : Pass"
    else
        print $1 " : Fail"
}'