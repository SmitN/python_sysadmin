#!/bin/bash
#Simple backup scripts to copy contains of ic-scripts/deployments into /ic-scripts-archive
#ONLY ALLOWED TO RUN on NON-PROD hosts
#Author: SN
#Version: 1.0
#May 1st, 2017

#Variables
SOURCE="/home/smitnaik/scripts/deployments/"
DESTINATION="/data/scripts-archive"
DAY=$(date +%Y-%m-%d)
BACK_FILE=IC_SCRIPTS_DEPLOYMENTS_BACKUP_$DAY.tgz

HOST=$(hostname -s)

#IF PLAN IS TO RUN THIS SCRIPT ONLY ON THIS LAB HOST THEN LOGIC CAN BE
#name="XYZ"
#if [[ $HOST != $name ]];then
#   echo " EXISTING "
#   exit 11
#fi

echo "+++++++++++++++++++++++++++++++++++++++++++++"

echo $DAY
echo $HOST
if [[ $HOST == sec1* ]] || [[ $HOST == sec2* ]] || [[ $HOST == tky* ]] || [[ $HOST == us* ]] ; then
   echo "THIS IS A PRODUCTION HOST EXITING "
   exit 11
fi

echo "Backing UP contains of $SOURCE to $DESTINATION "

/bin/tar -cpzf $DESTINATION/IC_SCRIPTS_DEPLOYMENTS_BACKUP_$DAY.tar.gz $SOURCE*

echo "Back up finished "
date

ls -lh $DESTINATION
