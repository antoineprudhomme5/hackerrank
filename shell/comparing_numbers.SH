read X
read Y

diff=$((X-Y))

if [[ $diff -lt 0 ]];
then
	echo "X is less than Y"
elif [[ $diff -gt 0 ]];
then 
	echo "X is greater than Y"
else
	echo "X is equal to Y"
fi