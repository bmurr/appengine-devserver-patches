# appengine-devserver-patches
Any patches that I use for Google AppEngine dev_appserver.

So far:
 - File watcher patch. This replaces the mtime_file_watcher on OSX with a file watcher which uses the watchdog library. 
