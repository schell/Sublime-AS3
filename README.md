AS3
===

A Sublime Text 2 package for writing pure AS3 projects. The language definition file was taken from Simon Gregory's awesome TextMate bundle. (https://github.com/simongregory/actionscript3-tmbundle)

Installation
------------
Just clone this repo in your packages folder: 
 
    git clone git@github.com:schell/Sublime-AS3.git 'AS3'
    
Usage
-----
You may want to use mxmlc or fcsh or some custom build script you've written, so AS3Build.py (the
script that builds your projects) looks in your current settings for a command template called as3_build_cmd.
This should be a python format string. By default as3_build_cmd is "mxmlc %(input)s -o %(output)". My
copy of mxmlc isn't in my path, so I've changed this in my User settings to be "/SDKs/Flex/bin/mxmlc %(input)s -o %(output)".

In order to build your project's main .as file, add the relative path (relative to your sublime-project file) of the main
.as and the path to the target output swf to your project's sublime-project file:

```json
"settings" : {
    "input" : "relative/path/to/entrypoint.as", // relative to your project directory...
    "output" : "relative/path/to/deploy.swf"
}
```

As3Build.py will grab these values and prefix them with the project directory, stick them into the build command
and then run them like any other build command.

Why?
----
After moving from TextMate I needed to build my AS3 projects, while still allowing my teammates to build it on their machines, hence all the relative path and command string stuff. I also wanted to learn about packages and syntax definition in Sublime Text 2.