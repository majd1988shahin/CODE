#include <linux/module.h>
#include <linux/version.h>
#include <linux/kernel.h>

static void __exit end_mod ( void ) /* Destructor */
{
	printk( KERN_INFO "\n");
	printk ( KERN_INFO " Module majd good bye 6...\n ");
}
module_exit ( end_mod );

MODULE_LICENSE ("GPL");
MODULE_AUTHOR ("MS");
MODULE_DESCRIPTION (" Test Driver Module : majd");
MODULE_SUPPORTED_DEVICE("testdevice");
MODULE_VERSION("1.0.0");