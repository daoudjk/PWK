#!/bin/bash

for name in $(cat list.txt);do
	host $name.microsoft.com|grep "has address" | cut -d" " -f1,4
done
