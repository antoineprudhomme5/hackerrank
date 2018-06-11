arr=()
while read line;
do
	[[ ! $line =~ [aA] ]] && arr+=($line)
done
echo ${arr[@]}