from fabric.api import *

# env.hosts = ['host', 'host2',]
# warn_only=True

env.user = 'root'
env.roledefs = {
   'master'  : ['192.168.45.187'],
   'slaves'  : ['192.168.45.188']  
}

def servers():
   """ Defines a list of servers to use for fabric """ 
   env.hosts = open('./dist/servers.list', 'r').readlines()

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
   """ Deploys host file in ./dist/hosts """ 
   put('./dist/hosts', '/etc/hosts')

def puppet_client():
   """ Runs apt to install puppet Client, this assumes apt is setup correctly """ 
   run('apt-get install -q -y puppet')

#Needs some work
def puppet_master():
   """ Runs apt to install puppet Master, this assumes apt is setup correctly """ 
   run('apt-get install -q -y puppetmaster') 

def puppet_run(hostn=''):
   """ Run puppet once checking into the master  server set by host file """
   run("puppet agent apply --server=master --no-daemonize --verbose --onetime")

def agent_enable():
   """ Enables agent by setting START=yes """ 
   run('sed -i s/START=no/START=yes/ /etc/default/puppet')

def agent_disable():
   """ Disables agent by setting  START=no """ 
   run('sed -i s/START=yes/START=no/ /etc/default/puppet')
   
   
@hosts('master')
def deploy_master():
   deploy_hosts()

@hosts('slaves')
def deploy_slaves():
   deploy_hosts()

