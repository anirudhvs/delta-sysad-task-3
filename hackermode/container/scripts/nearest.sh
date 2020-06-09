#!/bin/bash

echo '' > /home/ChiefCommander/nearest10
R=6371
CONV=0.01745
cLat=0.50098
cLon=1.34569

distance () {
aLat=$1
aLon=$2

dLat=$(echo "$aLat-$cLat" | bc)
dLon=$(echo "$aLon-$cLon" | bc)
A=$(echo "(s($dLat/2)*s($dLat/2))+(c($cLat)*c($aLat))*(s($dLon/2)*s($dLon/2))" | bc -l)

C=$(awk -v A=$A 'BEGIN{print 2*atan2(sqrt(A),sqrt(1-A))}')
#D= $(echo "$C*$R" | bc )
D=$(awk -v C=$C -v R=$R 'BEGIN{print C*R}')
echo $D
}
touch /home/ChiefCommander/temp
bash /home/ChiefCommander/finalattend.sh

cat /home/ChiefCommander/attendance_report | grep 'Army' > /home/ChiefCommander/temp

LINES=$(wc -l /home/ChiefCommander/temp | awk '{print $1}')
N=1

touch /home/ChiefCommander/tempDist
LINES=$(($LINES-1))
while [[ $N -le $LINES ]]
do 
aLatD=$(sed -n "$N"p /home/ChiefCommander/temp | awk '{print substr($3,4)}')
aLonD=$(sed -n "$N"p /home/ChiefCommander/temp | awk '{print substr($4,4)}')

aLatR=$(awk -v aLatD=$aLatD -v CONV=$CONV 'BEGIN{print aLatD*CONV}')
aLonR=$(awk -v aLonD=$aLonD -v CONV=$CONV 'BEGIN{print aLonD*CONV}')

Dist=$(distance $aLatR $aLonR )
VAR=$(sed -n "$N"p /home/ChiefCommander/temp | awk '{print $1" "$2}')
echo "$VAR $Dist" >> /home/ChiefCommander/tempDist

N=$(($N+1))

done

sort -n -k 3 /home/ChiefCommander/tempDist > /home/ChiefCommander/tempDistF


N=1

while [[ $N -le  10 ]]
do 

sed -n "$N"p /home/ChiefCommander/tempDistF >> nearest10
N=$(($N+1))

done

rm temp
rm tempDist
rm tempDistF

