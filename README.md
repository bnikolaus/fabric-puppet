puppet-setup
============

puppet-setup is deployment/management strategy for a common puppet implementation in debian wheezy using the fabric framework as a base.
Currently this is under development to allow for easy deployments to large infrastructures.


fabric can be installed by running "pip install fabric" in almost all python setups.

To see a list of all commands:

fab --list
Available commands:

    agent_disable    Disables agent by setting  START=no
    agent_enable     Enables agent by setting START=yes
    deploy_hosts     Deploys host file in ./dist/hosts
    deploy_master
    deploy_slaves
    distribute_keys  Distribute keys to servers
    generate_keys    Generate an SSH key to be used for password-less control
    puppet_client    Runs apt to install puppet Client, this assumes apt is setup correctly
    puppet_master    Runs apt to install puppet Master, this assumes apt is setup correctly
    puppet_run       Run puppet once checking into the master  server set by host file
    servers          Defines a list of servers to use for fabric




