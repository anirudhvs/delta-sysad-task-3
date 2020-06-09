#!/bin/bash

echo "Enabling Final Attendance"

cp -f /scripts/attendance.log /home/ChiefCommander/attendance.log
cp -f /scripts/finalattend.sh /home/ChiefCommander/finalattend.sh

cd /home/ChiefCommander
chown ChiefCommander attendance.log
chown ChiefCommander finalattend.sh
chmod 770 finalattend.sh
./finalattend.sh

chown ChiefCommander attendance_report

echo "* 6 * * * finalattendance" >> /var/spool/cron/crontabs/ChiefCommander

cd /scripts

echo "Done enabling Final Attendance"
