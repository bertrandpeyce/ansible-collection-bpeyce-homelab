
build: .build_vm .build_ssh_config

.build_vm:
	vagrant up

.build_ssh_config:
	#TODO: This step fails if run with `.build_vm`, there is debugging todo
	vagrant ssh-config > .vagrant_ssh_config

clean:
	vagrant destroy
	rm .vagrant_ssh_config

provision:
	#TODO: Get the ip dynamically
	ansible-playbook -i 192.168.121.85, test.yml --ask-vault-pass

test:
	pytest --connection=ssh --ssh-config=.vagrant_ssh_config --hosts=gitlab_server test.py
