#!/bin/bash

echo "Starting to Schedule Posts"

cp -f /scripts/post.sh /home/ChiefCommander/post.sh
cp -f /scripts/position.log /home/ChiefCommander/position.log
cd /home/ChiefCommander

chown ChiefCommander position.log

ITERATOR=1
while [[ $ITERATOR -le 50 ]]
do 

touch /home/Army$ITERATOR/post_alotted
chown Army$ITERATOR:ArmyGeneral /home/Army$ITERATOR/post_alotted
chmod 770 /home/Army$ITERATOR/post_alotted

touch /home/Navy$ITERATOR/post_alotted
chown Navy$ITERATOR:NavyMarshal /home/Navy$ITERATOR/post_alotted
chmod 770 /home/Navy$ITERATOR/post_alotted

touch /home/AirForce$ITERATOR/post_alotted
chown AirForce$ITERATOR:AirForceChief /home/AirForce$ITERATOR/post_alotted
chmod 770 /home/AirForce$ITERATOR/post_alotted

ITERATOR=$(($ITERATOR+1))

done

chown ChiefCommander post.sh
chmod 770 post.sh
./post.sh

echo "* * * * * autoSchedule" >> /var/spool/cron/crontabs/ChiefCommander

cd /scripts

echo "Done Scheduling posts"
