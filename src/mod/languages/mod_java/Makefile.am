include $(top_srcdir)/build/modmake.rulesam
MODNAME=mod_java

mod_LTLIBRARIES = mod_java.la
mod_java_la_SOURCES  = mod_java.cpp fluxpbx_java.cpp switch_swig_wrap.cpp modjava.c
mod_java_la_CFLAGS   = $(AM_CFLAGS)
mod_java_la_CPPFLAGS = $(JAVA_FLAGS) $(AM_CPPFLAGS)
mod_java_la_LIBADD   = $(switch_builddir)/libfluxpbx.la
mod_java_la_LDFLAGS  = -avoid-version -module -no-undefined -shared

# Without -fno-strict-aliasing, g++ generates invalid code for Java_org_fluxpbx_fluxpbxJNI_SWIGJavaSessionUpcast, which segfaults
mod_java_la_CFLAGS  += $(JAVA_FLAGS) -fno-strict-aliasing

CLASSES=src/org/fluxpbx/Launcher.java \
	src/org/fluxpbx/HangupHook.java \
	src/org/fluxpbx/DTMFCallback.java \
	src/org/fluxpbx/FluxpbxScript.java \
	src/org/fluxpbx/Event.java \
	src/org/fluxpbx/swig/*

BUILT_SOURCES=classes fluxpbx.jar

classes:
	mkdir -p classes
	javac -sourcepath src -d classes $(CLASSES)
fluxpbx.jar: classes
	jar cf fluxpbx.jar -C classes org

reswig:
	rm -f switch_swig_wrap.cpp
	swig3.0 -java -c++ -I../../../include -package org.fluxpbx.swig -outdir src/org/fluxpbx/swig -o switch_swig_wrap.cpp mod_java.i

install-data-local:
	cp fluxpbx.jar $(DESTDIR)@scriptdir@

