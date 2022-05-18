#!/bin/bash
#Simple Zone Transfer Bash Script
# $1 is the first argument given after the bash script
#check if argument was given, otherwise, print usage
#-z returns true if the length of the given variable is zero

if [ -z "$1" ]; then
	echo "[*] Simple Zone transfer script"
	echo "[*] Usage : $0 <domain name>"
	exit 0
fi

#if argument was given, identify the DNS servers for the domain.
#for each of the servers, attempt a zone transfer

for server in $(host -t ns $1 |cut -d" " -f4);do
	host -l $1 $server |grep "has address"
done
