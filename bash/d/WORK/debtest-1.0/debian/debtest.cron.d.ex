#
# Regular cron jobs for the debtest package
#
0 4	* * *	root	[ -x /usr/bin/debtest_maintenance ] && /usr/bin/debtest_maintenance
