AS3
===

A Sublime Text 2 package for writing pure AS3 projects. The language definition file was taken from Simon Gregory's awesome TextMate bundle. (https://github.com/simongregory/actionscript3-tmbundle)

Usage
-----
* Install this repo in your packages directory. 
* Restart ST2. 
* In order to build your project entry-point add some settings to your sublime-project file:

```json
"settings" : {
    "input" : "relative/path/to/entrypoint.as", // relative to your project directory...
    "output" : "relative/path/to/deploy.swf"
}
```

* Profit

Customizing
-----------
Currently the only thing you *should* have to customize your build process is change the path to mxmlc. In the AS3.sublime-build file just change "/SDKs/Flex/bin/mxmlc" (the second to last line) to wherever your mxmlc is...

Why?
----
After moving from TextMate I needed to build my AS3 projects and also wanted to learn about packages and syntax definition in Sublime Text 2.