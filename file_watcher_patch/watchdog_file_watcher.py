"""Monitors a directory tree for changes using watchdog library."""

import os
import threading
import time
import warnings
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from google.appengine.tools.devappserver2 import watcher_common


class ShutdownError(Exception):
    pass


class WatchdogFileWatcher(FileSystemEventHandler):
    """Monitors a directory tree for changes using watchdog library."""

    SUPPORTS_MULTIPLE_DIRECTORIES = False

    def __init__(self, directory):
        super(WatchdogFileWatcher, self).__init__()
        self._directory = directory

        self._watcher_ignore_re = None
        self._skip_files_re = None

        self._changes = set()

    def set_watcher_ignore_re(self, watcher_ignore_re):
        self._watcher_ignore_re = watcher_ignore_re

    def set_skip_files_re(self, skip_files_re):
        self._skip_files_re = skip_files_re

    def _path_ignored(self, file_path):
        dir, filename = os.path.split(file_path)
        basedir, dirname = os.path.split(dir)
        return any([
          watcher_common.ignore_file(file_path, self._skip_files_re,
                                     self._watcher_ignore_re),
          watcher_common.ignore_dir(basedir, dirname, self._skip_files_re),
          watcher_common.ignore_dir(basedir, dirname, self._watcher_ignore_re)
        ])

    def on_moved(self, event):
        super(WatchdogFileWatcher, self).on_moved(event)
        self.on_changed(event)

    def on_created(self, event):
        super(WatchdogFileWatcher, self).on_created(event)
        self.on_changed(event)

    def on_deleted(self, event):
        super(WatchdogFileWatcher, self).on_deleted(event)
        self.on_changed(event)

    def on_modified(self, event):
        super(WatchdogFileWatcher, self).on_modified(event)
        self.on_changed(event)

    def on_changed(self, event):
        what = 'directory' if event.is_directory else 'file'
        #import logging; logging.info("Changed %s: %s", what, event.src_path)

        if not event.is_directory:
          if not self._path_ignored(event.src_path):
            self._changes.add(event.src_path)

    def changes(self, timeout_ms=0):

        try:
            time.sleep(1)
            changes = set(self._changes)
            self._changes = set()
            #import logging; logging.info("Checked for changes, got {}".format(changes));
            return changes
        except ShutdownError:
            pass
        return set()

    def start(self):
        #import logging; logging.info("Start watchdog called. Watching {}".format(self._directory));
        self.observer = Observer()
        self.observer.schedule(self, self._directory,
                               recursive=True)
        self.observer.start()

    def quit(self):
        #import logging; logging.info("Quit watchdog called.");
        self.observer.stop()
        self.observer.join()
