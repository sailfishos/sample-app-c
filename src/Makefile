BINDIR = ${DESTDIR}/usr/bin
CC = gcc
PKG_CONFIG = pkg-config
PKG_NAMES = ssu-sysinfo
PKG_LIBS = $(shell $(PKG_CONFIG) --libs $(PKG_NAMES))
PKG_CFLAGS = $(shell $(PKG_CONFIG) --cflags $(PKG_NAMES))
LIBS += $(PKG_LIBS)
CFLAGS += $(PKG_CFLAGS)

c-sample: c-sample.c
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)

install:
	mkdir -p $(BINDIR)
	install -m755 c-sample $(BINDIR)

clean:
	rm c-sample
