.PHONY: all build clean provision ssh-config test

all: build ssh-config test clean

build:
	vagrant up

clean:
	vagrant destroy -f

provision:
	vagrant provision

ssh-config:
	vagrant ssh-config > .vagrant_ssh_config

test: 
	pytest --connection=ssh --ssh-config=.vagrant_ssh_config --hosts=kvmhost test.py
