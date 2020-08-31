#!/bin/bash

# Check if the script has been executed from the reservations/ directory
# Move the current directory to it if not in order to execute the script

FILE=../manage.py
if test -f "$FILE"; then
    cd ..
fi


# Loads all the JSON-fixtures available in the reservations/app/fixtures directory with the manage.py utility

python3 manage.py dumpdata auth.group --indent 4 > app/fixtures/0_group.json
status=$?

if [ $status -ne 0 ] ;then
    printf "(0_group.json)\n>>> ERROR: JSON-data export has failed  (Fixture import error: $status)\n"
    printf "You may check if the data is valid and put in 'reservations/app/fixtures'"
    exit $status
else
    printf "(0_group.json)\n>>> SUCCESS: Fixture JSON-data successfully exported\n"
fi

python3 manage.py dumpdata auth.user --indent 4 > app/fixtures/1_user.json
status=$?

if [ $status -ne 0 ] ;then
    printf "(1_user.json)\n>>> ERROR: JSON-data export has failed  (Fixture import error: $status)\n"
    printf "You may check if the data is valid and put in 'reservations/app/fixtures'"
    exit $status
else
    printf "(1_user.json)\n>>> SUCCESS: Fixture JSON-data successfully exported\n"
fi

python3 manage.py dumpdata app.artist --indent 4 > app/fixtures/2_artist.json
status=$?

if [ $status -ne 0 ] ;then
    printf "(2_artist.json)\n>>> ERROR: JSON-data export has failed  (Fixture import error: $status)\n"
    printf "You may check if the data is valid and put in 'reservations/app/fixtures'"
    exit $status
else
    printf "(2_artist.json)\n>>> SUCCESS: Fixture JSON-data successfully exported\n"
fi

python3 manage.py dumpdata app.types --indent 4 > app/fixtures/3_types.json
status=$?

if [ $status -ne 0 ] ;then
    printf "(3_types.json)\n>>> ERROR: JSON-data export has failed  (Fixture import error: $status)\n"
    printf "You may check if the data is valid and put in 'reservations/app/fixtures'"
    exit $status
else
    printf "(3_types.json)\n>>> SUCCESS: Fixture JSON-data successfully exported\n"
fi

python3 manage.py dumpdata app.artistType --indent 4 > app/fixtures/4_artisttype.json
status=$?

if [ $status -ne 0 ] ;then
    printf "(4_artisttype.json)\n>>> ERROR: JSON-data export has failed  (Fixture import error: $status)\n"
    printf "You may check if the data is valid and put in 'reservations/app/fixtures'"
    exit $status
else
    printf "(4_artisttype.json)\n>>> SUCCESS: Fixture JSON-data successfully exported\n"
fi

python3 manage.py dumpdata app.locality --indent 4 > app/fixtures/5_locality.json
status=$?

if [ $status -ne 0 ] ;then
    printf "(5_locality.json)\n>>> ERROR: JSON-data export has failed  (Fixture import error: $status)\n"
    printf "You may check if the data is valid and put in 'reservations/app/fixtures'"
    exit $status
else
    printf "(5_locality.json)\n>>> SUCCESS: Fixture JSON-data successfully exported\n"
fi

python3 manage.py dumpdata app.location --indent 4 > app/fixtures/6_location.json
status=$?

if [ $status -ne 0 ] ;then
    printf "(6_location.json)\n>>> ERROR: JSON-data export has failed  (Fixture import error: $status)\n"
    printf "You may check if the data is valid and put in 'reservations/app/fixtures'"
    exit $status
else
    printf "(6_location.json)\n>>> SUCCESS: Fixture JSON-data successfully exported\n"
fi

python3 manage.py dumpdata app.show --indent 4 > app/fixtures/7_show.json
status=$?

if [ $status -ne 0 ] ;then
    printf "(7_show.json)\n>>> ERROR: JSON-data export has failed  (Fixture import error: $status)\n"
    printf "You may check if the data is valid and put in 'reservations/app/fixtures'"
    exit $status
else
    printf "(7_show.json)\n>>> SUCCESS: Fixture JSON-data successfully exported\n"
fi

python3 manage.py dumpdata app.collaboration --indent 4 > app/fixtures/8_collaboration.json
status=$?

if [ $status -ne 0 ] ;then
    printf "(8_collaboration.json)\n>>> ERROR: JSON-data export has failed  (Fixture import error: $status)\n"
    printf "You may check if the data is valid and put in 'reservations/app/fixtures'"
    exit $status
else
    printf "(8_collaboration.json)\n>>> SUCCESS: Fixture JSON-data successfully exported\n"
fi

python3 manage.py dumpdata app.representation --indent 4 > app/fixtures/9_representation.json
status=$?

if [ $status -ne 0 ] ;then
    printf "(9_representation.json)\n>>> ERROR: JSON-data export has failed  (Fixture import error: $status)\n"
    printf "You may check if the data is valid and put in 'reservations/app/fixtures'"
    exit $status
else
    printf "(9_representation.json)\n>>> SUCCESS: Fixture JSON-data successfully exported\n"
fi

python3 manage.py dumpdata app.reservation --indent 4 > app/fixtures/a_reservation.json
status=$?

if [ $status -ne 0 ] ;then
    printf "(a_reservation.json)\n>>> ERROR: JSON-data export has failed  (Fixture import error: $status)\n"
    printf "You may check if the data is valid and put in 'reservations/app/fixtures'"
    exit $status
else
    printf "(a_reservation.json)\n>>> SUCCESS: Fixture JSON-data successfully exported\n"
fi

printf "\n------------------------------------------------------\n SUCCESS: All fixture JSON-data successfully exported \n------------------------------------------------------\n"
exit 0
