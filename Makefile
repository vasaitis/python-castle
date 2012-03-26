DESTDIR ?= /usr/lib64/python2.6/site-packages/acunu
SWIG ?= swig
SWIGFLAGS += -verbose -debug-csymbols -debug-lsymbols -I/usr/include -builtin

CFLAGS += -std=gnu99
CFLAGS += -ggdb -fPIC -DPIC -O2
# CFLAGS += -Wall -Wno-unused-function
# CFLAGS += -Werror
# TODO: don't hardcode the path to Python headers
CFLAGS += -D_FORTIFY_SOURCE=2 -I/usr/include/python2.6
LDFLAGS += -lcastle

OBJS = libcastle.py _libcastle.so libcastle_wrap.c

.PHONY: all
all: $(OBJS)

%_wrap.c %.py: %.i
	$(SWIG) $(SWIGFLAGS) -python $<

%.so: %.o
	$(LD) -shared $(LDFLAGS) -o $@ $<

_%.so: %_wrap.so
	cp $< $@

clean:
	$(RM) $(OBJS)

install: _libcastle.so libcastle.py __init__.py
	mkdir -p $(DESTDIR)
	install -m 0755 _libcastle.so $(DESTDIR)
	install -m 0644 libcastle.py $(DESTDIR)
	install -m 0644 castle.py $(DESTDIR)
	install -m 0644 __init__.py $(DESTDIR)
