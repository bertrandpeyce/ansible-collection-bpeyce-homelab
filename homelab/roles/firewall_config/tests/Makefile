
build:
	vagrant up

clean: 
	vagrant destroy

provision:
	vagrant provision

ssh_config: 
	vagrant ssh-config > .vagrant_ssh_config

test: 
	pytest --connection=ssh --ssh-config=.vagrant_ssh_config --hosts=firewall_config test.py
