# hide first 12 digits of credit cards
cat | sed -r 's/([0-9]{4} ){3}([0-9]{4})/**** **** **** \2/g'