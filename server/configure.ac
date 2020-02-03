dnl
dnl Configure script for fcserver
dnl
AC_INIT([fcserver], [1.05])
AC_CONFIG_AUX_DIR([autostuff])

AM_INIT_AUTOMAKE([-Wall foreign subdir-objects no-dist])
AM_SILENT_RULES([yes])

AC_CANONICAL_HOST
case "$host_os" in
    *linux*)
        # this is needed by usbdevice.h
        AC_DEFINE([OS_LINUX], [], [Building for Linux])
        ;;
    *)
        AC_MSG_ERROR([Only Linux is supported, not $host_os])
        ;;
esac

AC_PROG_CC
AC_PROG_CXX
AM_PROG_AR
AC_PROG_RANLIB

AC_CHECK_PROGS([PYTHON], [python3 python python2])

PKG_PROG_PKG_CONFIG
PKG_CHECK_MODULES([LIBUSB], [libusb-1.0])

FCSERVER_VERSION="${PACKAGE_NAME}-${PACKAGE_VERSION}"
gitrev=`git -C $srcdir rev-parse --short HEAD 2>/dev/null`
if test -n "$gitrev"; then
    FCSERVER_VERSION="${FCSERVER_VERSION}-${gitrev}"
fi
AC_DEFINE_UNQUOTED([FCSERVER_VERSION], ["$FCSERVER_VERSION"])

AC_OUTPUT([Makefile])
