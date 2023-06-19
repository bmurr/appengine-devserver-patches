Requests to `/_ah/gcs...` were not working due to missing `APPLICATION_ID` in os.environ.

See: https://issuetracker.google.com/issues/287752841

### To use
- Apply the patch environ_app_id.patch to `APPENGINE_ROOT/google/appengine/tools/devappserver2/util.py`
The command will look like `patch "$(gcloud info --format="value(installation.sdk_root)")/platform/google_appengine/google/appengine/tools/devappserver2/util.py" < environ_app_id.patch`.
