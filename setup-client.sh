wget http://apt.puppetlabs.com/puppetlabs-release-squeeze.deb
dpkg -i puppetlabs-release-squeeze.deb
# Install puppet
apt-get update
apt-get install -y puppet

edit hosts file

# Modify you 
vim /etc/puppet/puppet.conf 

[main]
server=puppet.example.com
 
[master]
certname=puppet.example.com
