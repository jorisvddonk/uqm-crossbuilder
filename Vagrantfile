Vagrant::Config.run do |config|
  config.vm.box = "ubuntu_quantal_x64"
  config.vm.box_url = "https://github.com/downloads/roderik/VagrantQuantal64Box/quantal64.box"
  config.vm.share_folder "v-root", "/uqmdev", "."
  config.vm.provision :puppet
  config.vm.customize ["modifyvm", :id, "--memory", 1024]
end