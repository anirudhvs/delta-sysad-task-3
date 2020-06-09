#!/bin/bash

echo "Generating users"


useradd -m -s /bin/bash ChiefCommander
useradd -m -s /bin/bash ArmyGeneral
useradd -m -s /bin/bash NavyMarshal
useradd -m -s /bin/bash AirForceChief


ITERATOR=1
while [[ $ITERATOR -le 50 ]]
do
useradd -m -s /bin/bash Army$ITERATOR 
ITERATOR=$(($ITERATOR+1))
done


ITERATOR=1
while [[ $ITERATOR -le 50 ]]
do
useradd -m -s /bin/bash Navy$ITERATOR 
ITERATOR=$(($ITERATOR+1))
done


ITERATOR=1
while [[ $ITERATOR -le 50 ]]
do
useradd -m -s /bin/bash AirForce$ITERATOR
ITERATOR=$(($ITERATOR+1))
done


echo "Done Generating users"
