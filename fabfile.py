from fabric.api import *

# env.hosts = ['host', 'host2',]
# warn_only=True

env.user = 'root'
env.roledefs = {
   'master' " : ['192.168.45.187'],
   'slaves' " : ['192.168.45.188'],  
}

def servers():
   env.hosts = open('servers.list', 'r').readlines()

# Key distribution and management
# local distribution

def generate_keys():
   """ Generate an SSH key to be used for password-less control """
   local("ssh-keygen -N '' -q -t rsa -f ~/.ssh/id_rsa")

def distribute_keys():
   """ Distribute keys to servers """
   local("ssh-copy-id -i ~/.ssh/id_rsa.pub %s@%s" % (env.user, env.host))

# Deployment Peices
# Hosts File for Communication 
def deploy_hosts():
   put('./dist/hosts', '/etc/hosts')

def puppet_client():
   run('apt-get install -q -y puppet')

#Needs some work
def puppet_master():
   run('apt-get install -q -y puppetmaster') 

# time to check in the boys
# ensure that this only run
def puppet_run(hostn=''):
   """ Run puppet once"""
   run("puppet agent apply --server=master --no-daemonize --verbose --onetime")


