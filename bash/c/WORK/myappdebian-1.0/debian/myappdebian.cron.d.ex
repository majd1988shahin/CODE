#
# Regular cron jobs for the myappdebian package
#
0 4	* * *	root	[ -x /usr/bin/myappdebian_maintenance ] && /usr/bin/myappdebian_maintenance
