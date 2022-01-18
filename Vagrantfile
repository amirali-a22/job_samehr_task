Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
  config.vm.box_check_update = true
  config.vm.network "public_network"
  config.vm.synced_folder ".", "/home/vagrant/app"
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.name = "Job Samehr Task Environment"
    vb.memory = "2024"
  end
  config.vm.provision "shell", path: "./vagrant/setup.sh"
end
