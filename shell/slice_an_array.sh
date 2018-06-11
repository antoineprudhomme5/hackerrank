arr=()
while read line;
do
    arr+=($line)
done
echo ${arr[@]:3:5}