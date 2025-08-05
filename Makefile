#TODO: take version into consideration

all: build install clean

build:
	ansible-galaxy collection build . --force
install:
	ansible-galaxy collection install bpeyce-homelab-1.0.0.tar.gz -p $(HOME)/.ansible/collections --force
clean:
	rm bpeyce-homelab-1.0.0.tar.gz
