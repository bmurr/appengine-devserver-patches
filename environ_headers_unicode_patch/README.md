Requests to `/_ah/queue_deferred` were not working due to encoding mismatch in environ headers.
This fixes that.

See: https://issuetracker.google.com/issues/219885365

Still needed as of `gcloud 426.0.0`

### To use
- Apply the patch enivron_headers.patch to `APPENGINE_ROOT/google/appengine/tools/devappserver2/util.py`
The command will look like `patch "$(gcloud info --format="value(installation.sdk_root)")/platform/google_appengine/google/appengine/tools/devappserver2/util.py" < environ_headers.patch`.
