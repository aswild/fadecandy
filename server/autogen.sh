#!/bin/sh
# Script to generate configure script and Makefiles from configure.ac and Makefile.am
# You can also use "autoreconf -fivs" for the same result, but this is slightly faster

set -xe
mkdir -p autostuff
aclocal --force
autoconf --force
automake --add-missing --force-missing
