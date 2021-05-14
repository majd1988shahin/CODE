CONFIG_MODULE_SIG=n
obj-m := majd05.o

KDIR := /usr/src/linux-headers-$(shell uname -r)
# echo $(uname -r)
PWD := $(shell pwd)
#Make-Aufruf
all:
	make clean
	$(MAKE) -C $(KDIR) M=$(PWD) modules
	make clean
	#make test
#Aufräumen - Löschen der erzeugten Dateien
clean:
	rm -rf *.mod *.o .*.cmd .tmp_versions Module.symvers
	rm -rf modules.order *.mod.c

test:
	sudo insmod majd05.ko mystring='majd' myintArray=5,7	
	dmesg | grep majd05
	echo ---------------------------------------
	sudo rmmod majd05.ko
	dmesg | grep majd05