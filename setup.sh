#!/bin/bash

# Setup Repos

# Setup Git
apt-get install git

# 
hostname master


apt-get install -y puppet puppet-common puppet-el puppet-testsuite \
	puppetmaster puppetmaster-common vim-puppet

# yum install puppet-server

apt-get install -y puppetmaster-passenger


