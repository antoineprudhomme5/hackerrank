# display chars from 2th to 7th
while read line;
do
    echo $line | cut -c 2-7
done