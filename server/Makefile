###########################################################################
# Fadecandy Server

TARGET := fcserver

CPP_FILES += \
	src/main.cpp \
	src/tcpnetserver.cpp \
	src/usbdevice.cpp \
	src/fcdevice.cpp \
	src/enttecdmxdevice.cpp \
	src/fcserver.cpp \
	src/version.cpp \
	src/tinythread.cpp \
	src/spidevice.cpp \
	src/apa102spidevice.cpp \
	src/httpdocs.cpp

INCLUDES += -Isrc
CLEAN_FILES += src/*.d src/*.o src/httpdocs.cpp
CPPFLAGS += -Wno-strict-aliasing

###########################################################################
# System Support

SYS := $(shell $(CXX) -dumpmachine)

ifneq (, $(findstring linux, $(SYS)))
UNAME := Linux
CPPFLAGS += -DOS_LINUX -pthread
LIBS += -pthread
endif
ifneq (, $(findstring mingw, $(SYS)))
UNAME := MINGW32
CPPFLAGS += -DOS_WINDOWS
endif
ifneq (, $(findstring darwin, $(SYS)))
UNAME := Darwin
CPPFLAGS += -DOS_DARWIN
endif

MINGW := $(findstring MINGW32, $(UNAME))
LIBS += -lstdc++ -lm
VERSION := $(shell git describe --match "fcserver-*")
CXXFLAGS += -DFCSERVER_VERSION=$(VERSION)

ifeq ($(UNAME), Darwin)
	# Mac OS X (32-bit build)
	LDFLAGS += -m32
	CPPFLAGS += -m32 -DHAVE_POLL_H

	ifeq ("$(shell which llvm-gcc)", "")
		# We want to support all the way back to OS 10.6 (Snow Leopard), which used gcc
		# instead of llvm. Omit some flags that this old gcc doesn't handle.
	else
		# Assume it's a new enough Mac OS version
		CPPFLAGS += -Wno-tautological-constant-out-of-range-compare
		CXXFLAGS += -std=gnu++0x
	endif
else
	# Everyone except ancient versions of gcc on Mac OS likes this flag...
	CXXFLAGS += -std=gnu++0x
endif

ifneq ("$(MINGW)", "")
	# Windows
	TARGET := $(TARGET).exe
	CPPFLAGS += -D_WIN32_WINNT=0x0501

	# Static build makes it portable but big, UPX packer decreases size a lot.
	LDFLAGS += -static
	PACK_CMD := upx\upx391w.exe $(TARGET)
endif

ifneq ("$(DEBUG)", "")
	# Debug build
	TARGET := debug-$(TARGET)
	CPPFLAGS += -g -DDEBUG -DENABLE_LOGGING
	PACK_CMD :=
else
	# Optimized build
	STRIP_CMD := strip $(TARGET)
	CPPFLAGS += -O2 -DNDEBUG
	LDFLAGS += -O2
endif

###########################################################################
# Built-in rapidjson

INCLUDES += -I.

###########################################################################
# Built-in libwebsockets

C_FILES += \
	libwebsockets/handshake.c \
	libwebsockets/libwebsockets.c \
	libwebsockets/parsers.c \
	libwebsockets/server-handshake.c \
	libwebsockets/server.c \
	libwebsockets/output.c \
	libwebsockets/sha-1.c \
	libwebsockets/base64-decode.c

# For lws_get_library_version(), which we don't use.
CPPFLAGS += -DLWS_LIBRARY_VERSION= -DLWS_BUILD_HASH=

# Disable a bunch of features
CPPFLAGS += -DLWS_NO_EXTENSIONS -DLWS_NO_CLIENT -DLWS_NO_WSAPOLL

INCLUDES += -Ilibwebsockets
CLEAN_FILES += libwebsockets/*.d libwebsockets/*.o

ifneq ("$(MINGW)", "")
	# Windows
	INCLUDES += -Ilibwebsockets/win32port/win32helpers
else
	# This is redundant on Windows, but we want it on other platforms
	CPPFLAGS += -DLWS_NO_DAEMONIZE
endif

###########################################################################
# libusb
INCLUDES += $(shell pkg-config --cflags libusb-1.0)
LIBS += $(shell pkg-config --libs libusb-1.0)

###########################################################################
# Build Rules

# Compiler options for C and C++
CPPFLAGS += -MMD $(INCLUDES)

# Compiler options for C++ only
CXXFLAGS += -felide-constructors -fno-exceptions -fno-rtti

OBJS := $(CPP_FILES:.cpp=.o) $(C_FILES:.c=.o)

print-%: ; @echo $* = $($*)
all: print-SYS $(TARGET)

# FIXME: A race condition between objects regeneration and their source mtime in make ?
$(TARGET): $(OBJS)
	$(CXX) $(LDFLAGS) -o $@ $(OBJS) $(LIBS)
	$(STRIP_CMD)
	$(PACK_CMD)
	rm -f src/version.o

-include $(OBJS:.o=.d)

src/httpdocs.cpp: http/* http/js/* http/css/*
	(cd http; python manifest.py) > $@

clean:
	rm -f $(CLEAN_FILES) $(TARGET)

.PHONY: clean all
