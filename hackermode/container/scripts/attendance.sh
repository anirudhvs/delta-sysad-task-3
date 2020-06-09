#!/bin/bash

echo "Initalising attendance"

cp -f /scripts/attendance.log /home/ChiefCommander/attendance.log
cp -f /scripts/prevAttend.sh /home/ChiefCommander/prevAttend.sh
cp -f /scripts/attend.sh /home/ChiefCommander/attend.sh

cd /home/ChiefCommander

chown ChiefCommander attendance.log
chown ChiefCommander attend.sh
chown ChiefCommander prevAttend.sh
chmod 770 attendance.log 
chmod 770 attend.sh
chmod 770 prevAttend.sh


./prevAttend.sh
./attend.sh

echo "* 6 *** attendance" >> /var/spool/cron/crontabs/ChiefCommander

rm prevAttend.sh

cd /scripts

echo "Done initialising attendance"
