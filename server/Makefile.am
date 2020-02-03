#
# Makefile for fcserver
#

AM_CFLAGS = -Wall -pthread
AM_CXXFLAGS = $(AM_CFLAGS)

# avoid warnings about 'u' being the default
ARFLAGS = cr

noinst_LIBRARIES = libwebsockets/libwebsockets.a
libwebsockets_libwebsockets_a_SOURCES = \
 libwebsockets/libwebsockets.h \
 libwebsockets/private-libwebsockets.h \
 libwebsockets/base64-decode.c \
 libwebsockets/handshake.c \
 libwebsockets/libwebsockets.c \
 libwebsockets/output.c \
 libwebsockets/parsers.c \
 libwebsockets/server-handshake.c \
 libwebsockets/server.c \
 libwebsockets/sha-1.c

libwebsockets_libwebsockets_a_CPPFLAGS = \
 -DLWS_LIBRARY_VERSION= -DLWS_BUILD_HASH= \
 -DLWS_NO_EXTENSIONS -DLWS_NO_CLIENT -DLWS_NO_WSAPOLL -DLWS_NO_DAEMONIZE

bin_PROGRAMS = fcserver
fcserver_SOURCES = \
 src/apa102spidevice.cpp src/apa102spidevice.h \
 src/enttecdmxdevice.cpp src/enttecdmxdevice.h \
 src/fast_mutex.h \
 src/fcdevice.cpp src/fcdevice.h \
 src/fcserver.cpp src/fcserver.h \
 src/httpdocs.cpp \
 src/main.cpp \
 src/opc.h \
 src/spidevice.cpp src/spidevice.h \
 src/tcpnetserver.cpp src/tcpnetserver.h \
 src/tinythread.cpp src/tinythread.h \
 src/usbdevice.cpp src/usbdevice.h \
 src/version.cpp src/version.h

fcserver_CPPFLAGS = -I$(srcdir)/src -I$(srcdir)/libwebsockets
fcserver_CXXFLAGS = $(AM_CXXFLAGS) $(LIBUSB_CFLAGS)
fcserver_LDADD = libwebsockets/libwebsockets.a $(LIBUSB_LIBS)

CLEANFILES = src/httpdocs.cpp
src/httpdocs.cpp:
	$(AM_V_GEN)$(PYTHON) $(srcdir)/http/manifest.py -o $@
