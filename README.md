##NodeJS Centos 6 RPM Package Script
==================

This script create a RPM package of NodeJS for Centos6. 

###Requires
  * make
  * wget
  * rpmbuild
  * g++ (for NodeJS compile)

###HowTo
  + Clone this repo
  + Open defines.mk file and change the ver=0.8.14 to the required version
  + Run the **make rpm** command and wait while the package is compiled. 

 The package will be created in ~/rpmbuild/RPMS/

###Thanks
 Thanks to Vibol Hou for this post and source http://vibol.hou.cc/installing-node-js-on-centos-6-3

  
