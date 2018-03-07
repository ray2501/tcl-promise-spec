#!/usr/bin/tclsh

set arch "noarch"
set base "promise-1.0.3"

set fileurl "https://sourceforge.net/projects/tcl-promise/files/promise-1.0.3.tm"

set var [list wget $fileurl -O $base.tm]
exec >@stdout 2>@stderr {*}$var

file mkdir $base
cd $base
file copy ../$base.tm .
cd ..

file delete -force $base.tm
set var [list tar czvf $base.tar.gz $base]
exec >@stdout 2>@stderr {*}$var

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb tcl-promise.spec]
exec >@stdout 2>@stderr {*}$buildit

#Remove source package
file delete -force $base
file delete -force $base.tar.gz

