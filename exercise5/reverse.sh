#!/bin/bash

for ip in $(seq 1 254); do
	host {ipaddress}.$ip | grep "microsoft" | cut -d" " -f1,5
done
