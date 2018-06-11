read N
total=0
for (( c=1; c<=$N; c++ ));
do
    read tmp
    total=$(($total+$tmp))
done
printf "%.3f\n" $(echo "$total/$N" | bc -l)