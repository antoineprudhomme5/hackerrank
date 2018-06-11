read
arr=$(cat)
arr=$(echo "${arr[*]}" | tr " " "^")
echo $(($arr))
