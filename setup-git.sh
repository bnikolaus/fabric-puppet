#!/bin/bash

# add git user
adduser git

# Setup SSH 
ssh root@master mkdir .ssh
scp ~/.ssh/id_rsa.pub root@master:/root/.ssh/authorized_keys

# Setting up git
apt-get install git-core
mkdir /home/git/.ssh

cp ~/.ssh/authorized_keys /home/git/.ssh/
root@debian:~/.ssh# chmod 600 /home/git/.ssh/*
root@debian:~/.ssh# chmod 700 /home/git/.ssh

# Setup Repos
/etc/puppet/modules
git --bare init
