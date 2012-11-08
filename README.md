This is a development environment intended to cross-build UQM for Windows within a VM.

The following tools are used to provide developers with a streamlined development environment:
* Vagrant (http://vagrantup.com/)
* Fabric (http://docs.fabfile.org/en/1.4.3/. Used to control the VM)

Puppet (http://docs.puppetlabs.com/) is used by Vagrant to provision a Virtual Machine.

#Requirements

* Vagrant
* Fabric

#Usage

1. fab init
2. fab download_uqm_src
3. fab build_uqm

#Installing Fabric on Windows

Installing Fabric on Windows can be difficult. Here's what you need to do:

1. Install Python 2.7
2. Install pycrypto (get a build from http://www.voidspace.org.uk/python/modules.shtml)
3. Install pywin32 (get a build from http://sourceforge.net/projects/pywin32/)
4. Install pip (http://www.pip-installer.org/en/latest/installing.html)
5. run 'pip install fabric'

# TODOs

* Support Project 6014, Balance Mod, etc.
* Move 'dirty hacks' to the default.pp Puppet Provision script
* Support for configurable mount points (e.g. allow users to mount existing SVN checkouts)
* Support for NSIS install scripts (for Project 6014)