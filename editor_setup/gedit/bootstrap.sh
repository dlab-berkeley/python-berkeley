#!/usr/bin/env bash

apt-get update
apt-get install -y gedit gedit-plugins gedit-developer-plugins rabbitvcs-gedit

# Another example: Apache install
# You'll also want to enable port forwarding (currently commented) in the
# Vagrantfile!

# apt-get install -y apache2
# rm -rf /var/www
# ln -fs /vagrant /var/www
