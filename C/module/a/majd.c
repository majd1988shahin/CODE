#include <linux/module.h>
#include <linux/version.h>
#include <linux/kernel.h>
static int __initdata hello3_data  = 0;
static int __init init_mod ( void ) /* Constructor */
{
	printk ( KERN_INFO "Module majd hallo 11 ...\n ");
	return hello3_data;
}
static void __exit end_mod ( void ) /* Destructor */
{
	printk ( KERN_INFO " Module majd good bye 22...\n ");
}
module_init ( init_mod );
module_exit ( end_mod );

MODULE_LICENSE ("GPL");
MODULE_AUTHOR ("MS");
MODULE_DESCRIPTION (" Test Driver Module : majd");
MODULE_SUPPORTED_DEVICE("testdevice");
MODULE_VERSION("1.0.0");
