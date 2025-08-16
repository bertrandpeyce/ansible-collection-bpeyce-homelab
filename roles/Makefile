.PHONY: test test_postfix

test: test_postfix test_kvm_host

test_postfix:
	$(MAKE) -C $(CURDIR)/postfix/tests 

test_kvm_host:
	$(MAKE) -C $(CURDIR)/kvm_host/tests
