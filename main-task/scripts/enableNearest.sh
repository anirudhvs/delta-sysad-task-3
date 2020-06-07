#!/bin/bash

echo "Enabling Nearest"

cd /home/ChiefCommander

cp -f /scripts/nearest.sh /home/ChiefCommander/nearest.sh

chown ChiefCommander /home/ChiefCommander/nearest.sh
chmod 770 /home/ChiefCommander/nearest.sh

echo "* 6 * * * nearest" >> /var/spool/cron/crontabs/ChiefCommander

cd /scripts

echo "Done Enabling Nearest"
