# replace thy by your (case insensitive)
cat | sed -r 's/(thy)/{\1}/gI'