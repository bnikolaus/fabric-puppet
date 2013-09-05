from fabric.api import *
import getpass

#
# env.hosts = ['host', 'host2',]
# warn_only=True

env.user = 'root'

# master and slave role declarations
env.roledefs = {
   'master'  : ['192.168.45.187'],
}

with open("./dist/servers.list") as f:
	env.roledefs['slaves'] = f.readlines()


env.parallel = 'True'
#env.password = getpass.getpass('Enter passwords: ')


# Example of a Host specific enties
# def servers():
#   """ Defines a list of servers to use for fabric """ 
#   env.hosts = open('./dist/servers.list', 'r').readlines()
# Key distribution and management from local server, if a key exists dont worry about running this  

def generate_keys():
   """ Generate an SSH key to be used for password-less control """
   local("ssh-keygen -N '' -q -t rsa -f ~/.ssh/id_rsa")

# Distribute local key to all servers
@roles('master', 'slaves')
def distribute_keys():
   """ Distribute keys to servers """
   local("./ssh-copy-id -i ~/.ssh/id_rsa.pub %s@%s" % (env.user, env.host))

# Hosts File for Communication 
def deploy_hosts():
   """ Deploys host file in ./dist/hosts """ 
   put('./dist/hosts', '/etc/hosts')

@roles('master', 'slaves')
def setup_ntp():
   """ Setup NTP """
   run('apt-get install -q -y ntp ntpdate')

def puppet_client():
   """ Runs apt to install puppet Client, this assumes apt is setup correctly """ 
   run('apt-get install -q -y puppet')

@roles('master')
def puppet_master():
   """ Runs apt to install puppet Master, this assumes apt is setup correctly """ 
   run('apt-get install -q -y puppetmaster') 

@roles('slaves')
def puppet_run():
   """ Run puppet once checking into the master  server set by host file """
   run("puppet agent apply --server=master.localdomain --no-daemonize --verbose --onetime")

def agent_enable():
   """ Enables agent by setting START=yes """ 
   run('sed -i s/START=no/START=yes/ /etc/default/puppet')

def agent_disable():
   """ Disables agent by setting  START=no """ 
   run('sed -i s/START=yes/START=no/ /etc/default/puppet')

@roles('slaves')
def puppet_cert_get():
   """ generate certs on slaves """
   run("puppet cert --generate `hostname`")

def puppet_cert_delete():
   """ delete certs on slaves """
   run("rm -rf /var/lib/puppet/ssl/certs/")


@roles('master')
def deploy_master():
   deploy_hosts()
   distribute_keys() 
   setup_ntp() 
   puppet_master()

@roles('slaves')
def deploy_slaves():
   deploy_hosts()
   distribute_keys() 
   setup_ntp() 
   puppet_client()
   puppet_run()
