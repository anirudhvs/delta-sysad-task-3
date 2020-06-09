#!/bin/bash

cd /home/ChiefCommander

#ARMY
ITERATOR=1
while [[ $ITERATOR -le 50 ]]
do
cat position.log | grep -w  "$(date +%Y-%m-%d)-00.00.00 Army$ITERATOR" | awk '{print $1" "$3" "$4}' > /home/Army$ITERATOR/post_alotted
ITERATOR=$(($ITERATOR+1))
done


#NAVY
ITERATOR=1
while [[ $ITERATOR -le 50 ]]
do
cat position.log | grep -w  "$(date +%Y-%m-%d)-00.00.00 Navy$ITERATOR" | awk '{print $1" "$3" "$4}' > /home/Navy$ITERATOR/post_alotted
ITERATOR=$(($ITERATOR+1))
done


#AIRFORCE
ITERATOR=1
while [[ $ITERATOR -le 50 ]]
do
cat position.log | grep -w  "$(date +%Y-%m-%d)-00.00.00 AirForce$ITERATOR" | awk '{print $1" "$3" "$4}' > /home/AirForce$ITERATOR/post_alotted
ITERATOR=$(($ITERATOR+1))
done

