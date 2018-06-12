# echo the firsts 4 chars
while read line;
do
    echo $line | cut -c1-4
done