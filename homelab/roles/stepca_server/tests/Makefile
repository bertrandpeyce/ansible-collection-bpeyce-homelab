
build:
	vagrant up

ssh-config:
	vagrant ssh-config > .vagrant_ssh_config

clean:
	vagrant destroy
	rm .vagrant_ssh_config

provision:
	vagrant provision

test: ssh-config
	pytest --connection=ssh --ssh-config=.vagrant_ssh_config --hosts=stepca test.py
