# print lines 2 by 2, separated by ;
cat | awk '{
    if (NR%2==0)
        printf $0"\n"
    else
        printf $0";"
}'