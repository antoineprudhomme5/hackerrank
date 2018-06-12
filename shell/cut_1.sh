# echo the 3th char of each string
while read line;
do
    echo $(echo $line | cut -c 3)
done