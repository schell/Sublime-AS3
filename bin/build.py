# This script is meant to set up some env vars for mxmlc or another
# as3 compilation situation.
# It looks for a file named as3pb.json with the following structure:
# {
#	  "input" : "the/relative/path/to/the/input.as",
#	  "output": "the/relative/path/to/the/output.swf"
# }
#
# In case it doesn't find that file, it'll try to do something clever. I hope.
#
# Author: Schell Scivally
# Usage: python build.py path/to/project path/to/backup/target/file.as nameOfBackupTarget.swf
#
import json, os, optparse, subprocess

parser = optparse.OptionParser()
parser.add_option("--project", help="Directory of AS3 project containing an as3pb.json config file.")
parser.add_option("--project-name", help="Name of AS3 project file containing config settings.")
parser.add_option("--input", default="",
	help="Input .as file. This is overridden by an input listed in a project file.")
parser.add_option("--output", default="",
	help="Output .swf file. This is overridden by an input listed in a project file.")
parser.add_option("--cmd", default="mxmlc",
	help="The path to mxmlc, example: /usr/local/bin/mxmlc")

opts, args = parser.parse_args()

input = ""
output = ""
cmd = "mxmlc"

if not opts.project is None and not opts.project_name is None:
	configFile = opts.project+"/"+opts.project_name

	if os.path.isfile(configFile):
		configText = open(configFile, "r").read()
		configJSON = json.loads(configText)
		settings = configJSON["settings"]
		input = opts.project+"/"+settings["input"]
		output = opts.project+"/"+settings["output"]

if not opts.cmd is None:
	cmd = opts.cmd


subprocess.call([cmd, input, "-o", output])

print "\nRead configuration in",opts.project+"/"+opts.project_name