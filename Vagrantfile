# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.synced_folder ".", "/vagrant"
  
  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "ansible/vagrant.yml"
    ansible.tags = ['setup']
    ansible.verbose = 'vvvv'
  end
end
