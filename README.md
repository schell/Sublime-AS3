AS3ProjectBuild
===============

A project building package for Sublime Text 2

Usage
-----
* Install this repo in your packages directory. 
* Restart ST2. 
* At the root of your as3 project create a file named "as3pb.json" that looks something like this:
    {
        "input" : "path/to/entrypoint.as",
        "output" : "path/to/deploy.swf"
    }
* Profit

Customizing
-----------
Currently the only thing you *should* have to customize is the path to mxmlc. In the AS3ProjectBuild.sublime-build file just change "/SDKs/Flex/bin/mxmlc" (the second to last line) to wherever your mxmlc is...