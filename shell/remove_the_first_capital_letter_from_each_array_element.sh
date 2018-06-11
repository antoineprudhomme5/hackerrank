arr=()
while read line;
do
	arr+=($(echo $line | sed s/^[A-Z]/\./ ))
done
echo ${arr[@]}