fcheck--()
{
for_check=$(cat /proc/sys/net/ipv4/ip_forward)
	if [[ $for_check == 0 ]];then
		clear
		echo -e "$out\nKernel Forwarding is Not Enabled\n$inp\nMake it So? (y or n)"
		read k_for_check
		case $k_for_check in
			y|Y)
			echo "1" > /proc/sys/net/ipv4/ip_forward ;;
		esac
	fi
}


ip_mac--()
{

##ipv4
#=`echo $input | awk -F. '{ if ( NF != 4 || length($0) > 15 || length ($0) < 7 || length($1) > 3 || length($2) > 3 || length($3) > 3 || length($4) > 3 ) print "FAIL" }'`

#ipv6
#=`echo $input | awk -F: '{ if ( NF != 8 || length($0) > 39 || length ($0) < 15 || length($1) > 4 || length($2) > 4 || length($3) > 4 || length($4) > 4 || length($5) > 4 || length($6) > 4 || length($7) > 4 || length($8) > 4 ) print "FAIL" }'`

##MAC
#=`echo $input | awk -F: '{ if ( NF != 6 || length($0) > 17 || length ($0) < 11 || length($1) > 2 || length($2) > 2 || length($3) > 2 || length($4) > 2 || length($5) > 2 || length($6) > 2 ) print "FAIL" }'`

case $1 in
	ip) var=$2
	echo $var | grep -v [^0-9.]
	if [ $? -ne 0 ];then
		ip_mac="fail"
	else
		for (( i = 1 ; i < 5 ; i++ ));do
			column=$(echo $var | cut -d . -f$i)
			if [[ $column -lt 0 || $column -gt 255 ]];then
				ip_mac="fail"
				break
			else
				ip_mac=
			fi

		done

		clear
		ip_mac=
	fi

	if [[ $ip_mac == "fail" ]];then
		echo -e "$wrn\nIP Address is not Valid"
		sleep 1
	fi;;

# 	mac) var=$2
# 	echo $var | grep -iv [^g-z:]
# 	if [ $? -ne 0 ];then
# 		ip_mac="fail"
# 	else
# 		ip_mac=
# 	fi
#
# 	if [[ -z $ip_mac ]];then
# 		for (( i = 1 ; i < 5 ; i++ ));do
# 			column=$(echo $var | cut -d . -f$i)
# 			if [[ $column -lt 0 || $column -gt 255 ]];then
# 				ip_mac="fail"
# 				break
# 			else
# 				ip_mac=
# 			fi
#
# 		done
#
# 	clear
# 	fi
#
# 	if [[ $ip_mac == "fail" ]];then
# 		echo -e "$wrn\nMAC Address is not Valid"
# 		sleep 1
# 	fi;;
esac
}


ipt_--()
{
## The basic premise behind this function is to have a basic overview and flush capability for iptables.
## It is in no way to be an all encompassing tool.
clear
echo -e "$hdr
~~~~~~~~~~~~~~~~~~~~~~~
IPTABLES Configurations
~~~~~~~~~~~~~~~~~~~~~~~$inp
1) List Tables

2) Flush Tables

P)revious Menu

M)ain Menu$hdr
~~~~~~~~~~~~~~~~~~~~~~~\n$inp"
read var
case $var in
	1) clear
	echo -e "$out"
	iptables-save | egrep -v "Generated by|COMMIT|Completed on"
	echo -e "$ins\nPress Enter to Continue"
	read
	ipt_--;;

	2) ipt_flush--;;

	p|P) routing--;;

	m|M) main_menu--;;

	*) ipt_--;;
esac
}


ipt_flush--()
{
clear
echo -e "$hdr
~~~~~~~~~~~~~~~~~~~~~~
  --Flush IPTABLES--
~~~~~~~~~~~~~~~~~~~~~~$inp
1) Filter Tables

2) NAT Tables

3) Mangle Tables

4) Raw Tables

5) Flush All 4 Tables

P)revious Menu

M)ain Menu$hdr
~~~~~~~~~~~~~~~~~~~~~~\n$inp"
read var
clear
case $var in
	1) iptables -t filter --flush
	echo -e "$out"
	iptables-save -t filter | egrep -v "Generated by|COMMIT|Completed on"
	sleep 2
	ipt_flush--;;

	2) iptables -t nat --flush
	echo -e "$out"
	iptables-save -t nat | egrep -v "Generated by|COMMIT|Completed on"
	sleep 2
	ipt_flush--;;

	3) iptables -t mangle --flush
	echo -e "$out"
	iptables-save -t mangle | egrep -v "Generated by|COMMIT|Completed on"
	sleep 2
	ipt_flush--;;

	4) iptables -t raw --flush
	echo -e "$out"
	iptables-save -t raw | egrep -v "Generated by|COMMIT|Completed on"
	sleep 2
	ipt_flush--;;

	5) iptables -t filter --flush
	iptables -t nat --flush
	iptables -t mangle --flush
	iptables -t raw --flush
	echo -e "$out"
	iptables-save | egrep -v "Generated by|COMMIT|Completed on"
	sleep 3
	ipt_flush--;;

	p|P) ipt_--;;

	m|M) main_menu--;;

	*) ipt_flush--;;
esac
}


k_for--()
{
clear
echo -e "$out
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Current Kernel Forwarding status is `cat /proc/sys/net/ipv4/ip_forward`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$inp
1) Turn ON Kernel Forwarding

2) Turn OFF Kernel Forwarding

P)revious Menu

M)ain Menu$out
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n$inp"
read var
case $var in
	1) echo "1" > /proc/sys/net/ipv4/ip_forward
	k_for--;;

	2) echo "0" > /proc/sys/net/ipv4/ip_forward
	k_for--;;

	p|P) routing--;;

	m|M) main_menu--;;

	*) k_for--;;
esac
}


routing--()
{
## The order of functions are for 2, 3 and 4 are: ap_pre_var--(), ap_setup--(), ap--()
## The order of functions for the DHCP server is: dhcp_pre_var--(), dhcp_svr--()
#rte_choice= Routing Option Variable for use with IPTABLES setups...
#k_for_check= Variable to determine if the user would liek to enable Kernel Forwarding
private= ## Wifi Range Extender trip variable
clear
echo -e "$hdr
~~~~~~~~~~~~~~~~~~~~~~~~~~
    --Routing Features--
~~~~~~~~~~~~~~~~~~~~~~~~~~$inp
1) IPTABLES Configuration

2) Kernel Forwarding

3) Wireless Vaccuum

4) StickyPot

5) WiFi Range Extender

6) DHCP Server

M)ain Menu$hdr
~~~~~~~~~~~~~~~~~~~~~~~~~~\n$inp"
read rte_choice
case $rte_choice in
	3|5) dev_parent="routing--"
	if [[ -z $pii ]];then
		no_dev-- monitor
	fi

	if [[ -z $ie ]];then
		no_dev-- managed
	fi

	case $rte_choice in
		3) ap_type=3 ;;
		5) ap_type=5 ;;
	esac

	fcheck--;;

	4) dev_parent="routing--"
	if [[ -z $pii ]];then
		no_dev-- monitor
	fi

	ap_type=4;;
esac

case $rte_choice in
	1) ipt_--;;

	2) k_for--;;

	3) ap_pre_var--
	ap_setup--;;

	4) ap_pre_var--
	ap_setup--;;

	5) private="yes"
	ap_pre_var--
	ap_setup--;;

	6) dhcp_pre_var--
	if [[ $ap_check != "on" ]]; then
		ap_pre_var--
	fi

	dhcp_svr--;;

	m|M) main_menu--;;

	*) routing--;;
esac
}
