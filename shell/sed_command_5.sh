# reverse credit card blocks
cat | sed -r 's/([0-9]{4})\s([0-9]{4})\s([0-9]{4})\s([0-9]{4})/\4 \3 \2 \1/g'