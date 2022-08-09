#!/bin/bash

#promt for username and user group

echo 'Please enter your username'
read name

echo 'Please enter your group'
read group1

#add user to root
sudo useradd $name

#create group
sudo groupadd $group1

#add user to group
sudo usermod -aG $group1 $name
