all: sample-app-c
%:
	$(MAKE) -C src $@
