#!/bin/bash

pwd=`pwd`


cat challenge_list.txt | while read c
do
	if [ -r ${c}/README.md ]
		then
			git add ${c}/*
		else
			echo $c problems 
		fi
done
