arr=()
while read line;
do
	arr+=($line)
done
echo ${#arr[@]}