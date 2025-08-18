
all: build ssh_config test clean

build:
	vagrant up

ssh_config:
	vagrant ssh-config > .vagrant_ssh_config

provision:
	vagrant provision

clean:
	vagrant destroy
	rm .vagrant_ssh_config

test:
	pytest --connection=ssh --ssh-config=.vagrant_ssh_config --hosts=gitlab test.py
