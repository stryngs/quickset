#!/bin/bash

source lib/accessPoints.sh
source lib/dhcps.sh
source lib/hellos.sh
source lib/mains.sh
source lib/nicControl.sh
source lib/routes.sh
source lib/attacks/arpSpoofs.sh
source lib/attacks/dnsSpoofs.sh
source lib/attacks/ferrets.sh
source lib/attacks/menus.sh
source lib/attacks/strips.sh
source lib/attacks/wifis.sh

## launcher
current_ver=3.8.2
rel_date="21 March 2021"
envir--
if [[ "$UID" -ne 0 ]];then
	echo -e "$wrn\nMust be ROOT to run this script"
	exit 87
fi

if [[ -z $1  ]]; then
	phys_dev= ## Physical NIC variable
	kill_mon= ## Variable to determine if the "killing a monitor mode option" has been selected
	dev_check= ## Nulled

	ie=$(route -en | grep UG | awk '{print $8}' | head -n1)
	if [[ -n $ie ]];then

    ### Added a cut because of loose :
		ie=$(ifconfig $ie | awk '{print $1}' | head -n1 | cut -d: -f1)
	fi

	pii=$(iwconfig | grep -i monitor | awk '{print $1}' | head -n1)
	greet--
else
	usage--
fi
