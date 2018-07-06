fractal() {
	n=$1
	a=()
	for i in {0..99};
	do
		a[$i]="_"
	done
	height=16
	indexes=(49)

	for (( f=0; f<5; f++ ));
	do
		if [[ $n > 0 ]];
		then
			n=$((n-1))
			for (( i=1; i<=$height; i++ ));
			do
				t=("${a[@]}")
				for index in "${indexes[@]}";
				do
					t[$index]="1"
				done
				echo "${t[@]}"
			done

			temp_indexes=()
			for index in "${indexes[@]}";
			do
				temp_indexes[${#temp_indexes[@]}]=$(($index-1))
				temp_indexes[${#temp_indexes[@]}]=$(($index+1))
			done
			indexes=("${temp_indexes[@]}")

			for (( i=1; i<=$height; i++ ));
			do
				t=("${a[@]}")
				for index in "${indexes[@]}";
				do
					t[$index]="1"
				done
				echo "${t[@]}"

				if [[ $i != $height ]];
				then
					for (( j=0; j<"${#indexes[@]}"; j++ ))
					do  
				   		if [[ $(($j%2)) == 0 ]];
				   		then
				   			indexes[$j]=$((${indexes[$j]}-1))
				   		else
				   			indexes[$j]=$((${indexes[$j]}+1))
				   		fi
					done
				fi
			done
		else
			for (( i=0; i<$(($height*2)); i++ ));
			do
				echo "${a[@]}"
			done
		fi
		height=$(($height/2))
	done
	echo "${a[@]}"
}
read n
fractal $n | tac | tr -d ' '