#!/bin/bash


cp /app/client.py /home/ChiefCommander/client.py

cp /app/client.py /home/ArmyGeneral/client.py
cp /app/client.py /home/NavyMarshal/client.py
cp /app/client.py /home/AirForceChief/client.py

chown ChiefCommander /home/ChiefCommander/client.py

chown ArmyGeneral /home/ArmyGeneral/client.py
chown NavyMarshal /home/NavyMarshal/client.py
chown AirForceChief /home/AirForceChief/client.py



ITERATOR=1

while [[ $ITERATOR -le 50 ]]
do

cp /app/client.py /home/Army$ITERATOR/client.py
cp /app/client.py /home/Navy$ITERATOR/client.py
cp /app/client.py /home/AirForce$ITERATOR/client.py

chown Army$ITERATOR /home/Army$ITERATOR/client.py
chown Navy$ITERATOR /home/Navy$ITERATOR/client.py
chown AirForce$ITERATOR /home/AirForce$ITERATOR/client.py

ITERATOR=$(($ITERATOR+1))

done
