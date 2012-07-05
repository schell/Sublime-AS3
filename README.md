AS3ProjectBuild
===============

An actionscript project building package for Sublime Text 2

Usage
-----
	* Install this repo in your packages directory. 
	* Restart ST2. 
	* Add some settings to your sublime-project file:

		"settings" : {
			"input" : "relative/path/to/entrypoint.as",
			"output" : "relative/path/to/deploy.swf"
		}

	* Profit

Customizing
-----------
Currently the only thing you *should* have to customize is the path to mxmlc. In the AS3ProjectBuild.sublime-build file just change "/SDKs/Flex/bin/mxmlc" (the second to last line) to wherever your mxmlc is...