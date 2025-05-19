build:
	vagrant up
	vagrant ssh-config > .vagrant_ssh_config
clean :
	vagrant destroy
provision:
	vagrant provision
test:
	pytest --connection=ssh --ssh-config=.vagrant_ssh_config --hosts=dev test.py
