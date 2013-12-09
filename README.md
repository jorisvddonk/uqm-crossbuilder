# UQM crossbuilder (mingw), Docker edition #

This project contains a Dockerfile which can be used to build an UQM cross compiler image for Docker.
Said image can be used to crosscompile UQM for Windows, using mingw on an Ubuntu (quantal) machine.

## Usage ##

Ensure you have Docker installed (see the official Docker documentation)

build the image:

    docker build -t uqmcrossbuilder .


run the image (container) to crosscompile UQM (*note: this will expose the UQM source directory on your local machine to the container. The container in turn **will** write to that directory as part of the build process. It might be a good idea to make a backup of your UQM source folder first, just to be sure that nothing bad will happen*):

    cd YOUR_UQM_SRC_BASEDIR
    docker run -v `pwd`:/uqm -i uqmcrossbuilder

Your UQM source directory should now contain an uqm.exe or uqm-debug.exe file!

## Advanced options ##
You can pass some options to the container, like you'd expect when running UQM's build scripts traditionally:

    docker run -v `pwd`:/uqm -i uqmcrossbuilder uqm clean


## TODOs ##

* Make a copy of the UQM source directories prior to building so that no changes will be written to the user's UQM source tree
* Clean up / document / test
* Merge recent changes from [oldlaptop/uqm-crossbuilder](https://github.com/oldlaptop/uqm-crossbuilder) if needed. Not sure.


## Attribution ##

Large parts of this project were written by *oldlaptop* and *Roisack*: https://github.com/oldlaptop/uqm-crossbuilder. You might not be able to see their work in here, but that's probably just because of the different folder structure and the offloading of various functionalities to Docker. Trust me, 99% of the hard work in getting a crosscompiler working had been done by them.