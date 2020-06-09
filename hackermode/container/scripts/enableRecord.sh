#!/bin/bash

echo "Enabling Record"

cp -f /scripts/record.sh /home/ArmyGeneral/record.sh
cp -f /scripts/record.sh /home/NavyMarshal/record.sh
cp -f /scripts/record.sh /home/AirForceChief/record.sh


echo "alias record=\"bash /home/ArmyGeneral/record.sh\"" >> /home/ArmyGeneral/.bashrc
echo "alias record=\"bash /home/NavyMarshal/record.sh\"" >> /home/NavyMarshal/.bashrc
echo "alias record=\"bash /home/AirForceChief/record.sh\"" >> /home/AirForceChief/.bashrc

chown ArmyGeneral:ArmyGeneral /home/ArmyGeneral/record.sh
chown NavyMarshal:NavyMarshal /home/NavyMarshal/record.sh
chown AirForceChief:AirForceChief /home/AirForceChief/record.sh
chmod 770 /home/ArmyGeneral/record.sh
chmod 770 /home/NavyMarshal/record.sh
chmod 770 /home/AirForceChief/record.sh

echo "Done Enabling Record"
