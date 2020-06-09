#!/bin/bash

echo "Managing Permissions"

usermod -aG ArmyGeneral,NavyMarshal,AirForceChief ChiefCommander

chmod 770 -R /home/ChiefCommander

chmod 770 -R /home/ArmyGeneral
chmod 770 -R /home/NavyMarshal
chmod 770 -R /home/AirForceChief

chown ArmyGeneral:ArmyGeneral /home/ArmyGeneral
chown NavyMarshal:NavyMarshal /home/NavyMarshal
chown AirForceChief:AirForceChief /home/AirForceChief
#ARMY
ITERATOR=1
while [[ $ITERATOR -le 50 ]]
do
chown Army$ITERATOR:ArmyGeneral -R /home/Army$ITERATOR
chmod 770 -R /home/Army$ITERATOR
ITERATOR=$(($ITERATOR+1))
done

#NAVY
ITERATOR=1
while [[ $ITERATOR -le 50 ]]
do
chown Navy$ITERATOR:NavyMarshal -R /home/Navy$ITERATOR
chmod 770 -R /home/Navy$ITERATOR
ITERATOR=$(($ITERATOR+1))
done

#AIRFORCE
ITERATOR=1
while [[ $ITERATOR -le 50 ]]
do
chown AirForce$ITERATOR:AirForceChief -R /home/AirForce$ITERATOR
chmod 770 -R /home/AirForce$ITERATOR
ITERATOR=$(($ITERATOR+1))
done

echo "Done Managing Permissions"
