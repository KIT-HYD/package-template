# package-template

[![Build Status](https://travis-ci.org/KIT-HYD/package-template.svg?branch=master)](https://travis-ci.org/KIT-HYD/package-template)
[![Documentation Status](https://readthedocs.org/projects/hyd-template/badge/?version=latest)](http://hyd-template.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/KIT-HYD/package-template/branch/master/graph/badge.svg)](https://codecov.io/gh/KIT-HYD/package-template)

<hr>
The audience for this project is the 
Hydrology group at KIT (https://hyd.iwg.kit.edu). However this is simply a 
setuptools driven project template, which can be used for any purpose.
<hr>
The documentation can be found at: http://hyd-template.readthedocs.io <br>
<br>
This template can be used to publish your own Python code and make it usable 
in other projects. Following this template your own code will:

  * be installable via pip
  * install all its requirements automatically
  * have a valid license and attribution information
  * obviously be accessible on GitHub
  * add unittest to provide code safety
  * use Travis-CI to run the tests automatically
  * use ReadTheDocs to add proper documentation to your project.
  
The main benefits are the tremendously improved usability of your code. 
Potential users can install your package with one line of code and see if 
building works, the tests run without error and how much of your code they 
cover. Last but not least, with [GitHubPages](https://pages.github.com) 
or [Read the Docs](https://readthedocs.org) you have two great tools to 
supply your user with any kind of additional information.

## General Structure

So how does this packages look like? 

First of all, on the main project level you will find a number of important 
files and folders:

The first and most important folder will contain the Python package itself.
This is what will be installed at the users computer in case he installs your 
package using pip. Anything outside of this folder is used to setup the Git 
project, produce meta-data for the Python Package Index (PyPI) and will 
contain the documentation. 
 
<table class="table table-striped">
<tr><th>root folder</th><th>Description</th></tr>
<tr><td>package_template</td><td>This is your actual Python project 
folder</td></tr>
<tr><td>docs</td><td>This is the folder used for producing 
documentation.</td></tr>
<tr><td>README.md</td><td>use this file to produce a first overview 
for your project. Keep in mind that this is the first (and maybe only) page 
the user will visit.
</td></tr>
<tr><td>LICENSE</td><td>This is the MIT license. Keep it or replace it</td></tr>
<tr><td>.gitignore</td><td>git file. Specify all file types that 
should not be synchronized with the package, like data, config or development
 files</td></tr>
<tr><td>MANIFEST.in</td><td>This files 'includes' all non-python files that 
shall be installed along with the package, when installed using pip. This is 
typically the README.md or LICENSE file
</td></tr>
<tr><td>requirements.txt</td><td>This file should contain all Python 
dependencies for your package. pip will take care of installing them. 
Each dependency goes into its own line. If a minimum version is 
required, place it like: `numpy>=0.12` to install at least Version 0
.12 of numpy</td></tr>
<tr><td>requirements-rtd.txt</td><td>These are slightly different 
requirements needed on the readthedocs.org server to build the 
documentation correctly.</td></tr>
<tr><td>VERSION</td><td>place the version number here. You could e.g. 
increment the number whenever you push a new version on PyPI or onto a 
'stable' branch in GitHub. I do it this way to not push every litte bugfix or
 typo fix into a new version.
</td></tr>
<tr><td>.travis.yml</td><td>This is the configuration file for 
Travis-CI. You will need to log into [Travis](https://travis-ci.org) 
with you github account to enable automatic buildings</td></tr>
<tr><td>setup.py</td><td>This is the main installation file. pip will 
run exactly this file after installing the requirements. Everything 
that is necessary to make your package work, like generating default 
configuration or whatever, should go into this file. Do not fortget to adapt 
this file to your needs. This file will also set up all the meta-data for PyPI
</td></tr>
</table>