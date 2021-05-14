obj-m += majd01.o
all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules
clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
test:
	# We put a — in front of the rmmod command to tell make to ignore
	# an error in case the module isn’t loaded.
	# Insert the module
	sudo insmod majd01.ko
	# Display the kernel log
	dmesg
	sudo rmmod majd01
	# Clear the kernel log without echo
	sudo dmesg -C
