build:
	vagrant up

clean:
	vagrant destroy

provision:
	vagrant provision

ssh-config:
	vagrant ssh-config > .vagrant_ssh_config

test: 
	pytest --connection=ssh --ssh-config=.vagrant_ssh_config --hosts=postfix test.py
