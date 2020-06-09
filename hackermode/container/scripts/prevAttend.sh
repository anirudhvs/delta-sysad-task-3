#!/bin/bash

cd /home/ChiefCommander

#ARMY
touch /home/ArmyGeneral/attendance_record

touch temp.log
cat attendance.log | grep "Army" > temp.log

CUR="$(date +%s)"

N=1
until [[ $(date -d $(sed -n "$N"p temp.log | awk '{print substr($1,2,11)}') +%s ) -le $CUR ]]
do

if [[ "$(sed -n "$N"p temp.log | awk '{print $3}')" = "YES" ]]
then 
DATE=$(sed -n "$N"p temp.log | awk '{print substr($1,0,12)}')
MEMBER=$(sed -n "$N"p temp.log | awk '{print $2}')
POST=$( cat position.log | grep -w  "$DATE-00.00.00 $MEMBER" | awk '{print $3" "$4}')
echo "$DATE $MEMBER $POST" >> /home/ArmyGeneral/attendance_record
fi

N=$(($N+1))

done
rm temp.log

chown ArmyGeneral:ArmyGeneral /home/ArmyGeneral/attendance_record


#NAVY

touch /home/NavyMarshal/attendance_record

touch temp.log
cat attendance.log | grep "Navy" > temp.log

N=1
until [[ $(date -d $(sed -n "$N"p temp.log | awk '{print substr($1,2,11)}') +%s ) -le $CUR ]]
do

if [[ "$(sed -n "$N"p temp.log | awk '{print $3}')" = "YES" ]]
then 
DATE=$(sed -n "$N"p temp.log | awk '{print substr($1,0,12)}')
MEMBER=$(sed -n "$N"p temp.log | awk '{print $2}')
POST=$( cat position.log | grep -w  "$DATE-00.00.00 $MEMBER" | awk '{print $3" "$4}')
echo "$DATE $MEMBER $POST" >> /home/NavyMarshal/attendance_record
fi

N=$(($N+1))

done
rm temp.log

chown NavyMarshal:NavyMarshal /home/NavyMarshal/attendance_record



#AIRFORCE

touch /home/AirForceChief/attendance_record
touch temp.log
cat attendance.log | grep "AirForce" > temp.log


N=1
until [[ $(date -d $(sed -n "$N"p temp.log | awk '{print substr($1,2,11)}') +%s ) -le $CUR ]]
do

if [[ "$(sed -n "$N"p temp.log | awk '{print $3}')" = "YES" ]]
then 
DATE=$(sed -n "$N"p temp.log | awk '{print substr($1,0,12)}')
MEMBER=$(sed -n "$N"p temp.log | awk '{print $2}')
POST=$( cat position.log | grep -w  "$DATE-00.00.00 $MEMBER" | awk '{print $3" "$4}')
echo "$DATE $MEMBER $POST" >> /home/AirForceChief/attendance_record
fi

N=$(($N+1))

done
rm temp.log

chown AirForceChief:AirForceChief /home/AirForceChief/attendance_record
