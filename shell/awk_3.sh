# for each student, calculate the average of his notes
# and print his grade
cat | awk '{
    total=$2+$3+$4
    avg=total/3
    grade="FAIL"
    if (avg >= 80)
        grade="A"
    else if (avg >= 60)
        grade="B"
    else if (avg >= 50)
        grade="C"
    print $0 " : " grade
}'