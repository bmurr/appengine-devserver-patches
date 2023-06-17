Uses watchdog (https://github.com/gorakhargosh/watchdog) to watch for file system events.

The default mtime_file_watcher was very resource intensive, causing my Macbook's fan to spin like a jet engine even when it should be idle.
Watchdog uses the native MacOS FSEvents to detect file changes, which is more efficient.


Related articles:
  - https://medium.com/lumapps-engineering/appengine-on-macos-is-a-cpu-hog-heres-how-to-solve-this-problem-with-another-python-native-9f2a6dc5c960

### To use
- Apply the patch file_watcher.patch to `APPENGINE_ROOT/google/appengine/tools/devappserver2/file_watcher.py`
The command will look like `patch "$(gcloud info --format="value(installation.sdk_root)")/platform/google_appengine/google/appengine/tools/devappserver2/file_watcher.py" < file_watcher.patch`.
- Place watchdog_file_watcher.py in `APPENGINE_ROOT/google/appengine/tools/devappserver2/`

### Caveats:
  - Little to no testing done.
  - Changes in symlinked files are not tracked?

