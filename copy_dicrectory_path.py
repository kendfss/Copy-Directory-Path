import sublime
import sublime_plugin
import os


class CopyDirectoryPathCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if len(self.view.file_name()) > 0:
            path = os.path.dirname(self.view.file_name())
            sublime.set_clipboard(path)
            sublime.status_message("Copied file's directory path")

    def is_enabled(self):
        return self.view.file_name() is not None and len(self.view.file_name()) > 0
