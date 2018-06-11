read exp
v=$(echo $exp | bc -l)
printf "%.3f\n" $v