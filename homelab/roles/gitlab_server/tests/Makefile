
build:
	vagrant up
	vagrant ssh-config > .vagrant_ssh_config

clean:
	vagrant destroy
	rm .vagrant_ssh_config

provision:
	ansible-playbook -i 192.168.121.85, test.yml --ask-vault-pass
	#vagrant provision

test:
	pytest --connection=ssh --ssh-config=.vagrant_ssh_config --hosts=gitlab_server test.py
