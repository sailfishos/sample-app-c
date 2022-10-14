BINDIR = ${DESTDIR}/usr/bin
PKG_CONFIG = pkg-config
PKG_NAMES = ssu-sysinfo
PKG_LIBS = $(shell $(PKG_CONFIG) --libs $(PKG_NAMES))
PKG_CFLAGS = $(shell $(PKG_CONFIG) --cflags $(PKG_NAMES))
LIBS += $(PKG_LIBS)
CFLAGS += $(PKG_CFLAGS)

all: sample-app-c
sample-app-c: sample-app-c.c
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)

install:
	install -Dm755 -t $(BINDIR) sample-app-c

clean:
	rm sample-app-c
