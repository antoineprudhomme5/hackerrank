arr=()
while read line || [ -n "$line" ];
do
    arr+=($line)
done
arr=("${arr[@]}" "${arr[@]}" "${arr[@]}")
echo ${arr[@]}