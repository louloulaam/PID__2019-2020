#!/bin/bash

# Check if the script has been executed from the reservations/ directory
# Move the current directory to it if not in order to execute the script

FILE=../manage.py
if test -f "$FILE"; then
    cd ..
fi


# Loads all the JSON-fixtures available in the reservations/app/fixtures directory with the manage.py utility

for file in app/fixtures/*
do
    python3 manage.py loaddata $file
    status=$?

    if [ $status -ne 0 ] ;then
        printf "($file >>> Fixture import error: $status)\n>>> ERROR: JSON-data import has failed\n"
        printf "You may check if the data is valid and put in 'reservations/app/fixtures'"
        exit $status
    else
        printf "($file)\n>>> SUCCESS: Fixture JSON-data successfully imported\n"
    fi
done

printf "\n------------------------------------------------------\n SUCCESS: All fixture JSON-data successfully imported \n------------------------------------------------------\n"
exit 0
