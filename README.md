AS3
===

A Sublime Text 2 package for writing pure AS3 projects. The language definition file was taken from Simon Gregory's awesome TextMate bundle. (https://github.com/simongregory/actionscript3-tmbundle)

Installation
------------
Just clone this repo in your packages folder: 
 
    git clone git@github.com:schell/Sublime-AS3.git 'AS3'
    
Usage
-----
In order to build your project's entry-point, add some settings to your sublime-project file:

```json
"settings" : {
    "input" : "relative/path/to/entrypoint.as", // relative to your project directory...
    "output" : "relative/path/to/deploy.swf"
}
```

Profit.

Customizing
-----------
Currently the only thing you *should* have to customize in the build process is the path to mxmlc. In the AS3.sublime-build file just change "/SDKs/Flex/bin/mxmlc" (the second to last line) to wherever your mxmlc is...

Why?
----
After moving from TextMate I needed to build my AS3 projects and also wanted to learn about packages and syntax definition in Sublime Text 2.