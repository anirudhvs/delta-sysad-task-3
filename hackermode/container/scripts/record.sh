#!/bin/bash

DAYNUM=$1

if [[ $DAYNUM -ge $(date +%u) ]]
then
X=7
else
X=14
fi

case $DAYNUM in

1) DAY="monday-$X days" ;;
2) DAY="tuesday-$X days" ;;
3) DAY="wednesday-$X days" ;;
4) DAY="thursday-$X days" ;;
5) DAY="friday-$X days" ;;
6) DAY="saturday-$X days";;
7) DAY="sunday-$X days" ;;
esac

DATE=$(date -d"$DAY" +"%Y-%m-%d")

cat /home/$USER/attendance_record | grep "+$DATE"
