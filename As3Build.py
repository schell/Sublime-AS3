import sublime, sublime_plugin
import os

class As3BuildCommand(sublime_plugin.WindowCommand):
    def get_project_dir(self, filename):
        lastSearchAt = ''
        searchAt = os.path.dirname(filename)
        while searchAt != lastSearchAt:
            # Update our loop params...
            lastSearchAt = searchAt
            searchAt = os.path.dirname(searchAt)
            # Search the current directory for project files...
            ls = os.listdir(searchAt)
            for entry in ls:
                if 'sublime-project' in entry:
                # We found the project file...
                    return searchAt
        return ''

    def run(self):
        if self.window.active_view():
            # Get the name + path of the file we're editing...
            filename = str(self.window.active_view().file_name())
            # Get the user's settings for input and output and a command template...
            settings = sublime.active_window().active_view().settings()

            # Set up our default vars...
            input = settings.get('input', filename)
            # Could use regex here to make sure .as is at the end of the string
            # but meh...
            output = settings.get('output', input.replace('.as', '.swf'))

            # The default command template...
            cmd = settings.get('as3_build_cmd', "mxmlc %(input)s -o %(output)s")

            # Now find the location of the first sublime-project file...
            project_dir = self.get_project_dir(filename)

            # Prefix the input and output with the project directory...
            input = project_dir + '/' + input
            output = project_dir + '/' + output

            # Now construct the command...
            build_cmd_string = cmd % {'input':input, 'output':output}
            build_cmd = build_cmd_string.split(' ')
            
            # Call the normal build command...
            self.window.run_command('exec', {'cmd' : build_cmd})
