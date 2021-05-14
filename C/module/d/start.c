#include <linux/module.h>
#include <linux/version.h>
#include <linux/kernel.h>
static int __initdata hello3_data  = 0;
static int __init init_mod ( void ) /* Constructor */
{
	printk( KERN_INFO "\n");
	printk ( KERN_INFO "Module majd hallo 6 ...\n ");
	return hello3_data;
}
module_init ( init_mod );
