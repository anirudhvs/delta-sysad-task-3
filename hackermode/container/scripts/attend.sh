#!/bin/bash

cd /home/ChiefCommander


#ARMY
touch temp.log
CUR="+$(date +"%Y-%m-%d")"
cat attendance.log | grep "$CUR-06.00.00 Army" > temp.log

MAX=$(wc -l temp.log | awk '{print $1}')

N=1
while [[ $N -le $MAX ]]
do

if [[ "$(sed -n "$N"p temp.log | awk '{print $3}')" = "YES" ]]
then 
MEMBER=$(sed -n "$N"p temp.log | awk '{print $2}')
POST=$( cat position.log | grep -w  "$CUR-00.00.00 $MEMBER" | awk '{print $3" "$4}')
echo "$CUR $MEMBER $POST" >> /home/ArmyGeneral/attendance_record
fi

N=$(($N+1))

done

rm temp.log


#NAVY
touch temp.log
CUR="+$(date +"%Y-%m-%d")"
cat attendance.log | grep "$CUR-06.00.00 Navy" > temp.log

MAX=$(wc -l temp.log | awk '{print $1}')

N=1
while [[ $N -le $MAX ]]
do

if [[ "$(sed -n "$N"p temp.log | awk '{print $3}')" = "YES" ]]
then 
MEMBER=$(sed -n "$N"p temp.log | awk '{print $2}')
POST=$( cat position.log | grep -w  "$CUR-00.00.00 $MEMBER" | awk '{print $3" "$4}')
echo "$CUR $MEMBER $POST" >> /home/NavyMarshal/attendance_record
fi

N=$(($N+1))

done

rm temp.log


#AIRFORCE
touch temp.log
CUR="+$(date +"%Y-%m-%d")"
cat attendance.log | grep "$CUR-06.00.00 AirForce" > temp.log

MAX=$(wc -l temp.log | awk '{print $1}')

N=1
while [[ $N -le $MAX ]]
do

if [[ "$(sed -n "$N"p temp.log | awk '{print $3}')" = "YES" ]]
then 
MEMBER=$(sed -n "$N"p temp.log | awk '{print $2}')
POST=$( cat position.log | grep -w  "$CUR-00.00.00 $MEMBER" | awk '{print $3" "$4}')
echo "$CUR $MEMBER $POST" >> /home/AirForceChief/attendance_record
fi

N=$(($N+1))

done

rm temp.log
