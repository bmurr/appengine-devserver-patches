# appengine-devserver-patches
Any patches that I use for Google AppEngine dev_appserver.
My primary AppEngine projects are still using the Python2.7 runtime, so these patches may or may not be valid for you.

## file_watcher_patch

This replaces the mtime_file_watcher on MacOS with a file watcher which uses the watchdog library. 
 
## environ_headers_unicode_patch

Requests to `/_ah/queue_deferred` were not working due to encoding mismatch in environ headers. This fixes that.
See: https://issuetracker.google.com/issues/219885365

Seems to still be required as of gcloud 426.0.0

## environ_app_id_patch

Requests to `/_ah/gcs...` were not working due to missing `APPLICATION_ID` in os.environ.

See: https://issuetracker.google.com/issues/287752841

Seems to still be required as of gcloud 435.0.1
