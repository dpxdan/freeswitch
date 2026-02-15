#!/bin/sh
#
# fluxpbx.sh - startup script for fluxpbx on FreeBSD
#
# This goes in /usr/local/etc/rc.d and gets run at boot-time.

case "$1" in

    start)
    if [ -x /usr/local/fluxpbx/bin/fluxpbx ] ; then
        echo -n " fluxpbx"
        /usr/local/fluxpbx/bin/fluxpbx -nc &
    fi
    ;;

    stop)
    if [ -x /usr/local/fluxpbx/bin/fluxpbx ] ; then
        echo -n " fluxpbx"
        /usr/local/fluxpbx/bin/fluxpbx -stop &
    fi
    ;;

    *)
    echo "usage: $0 { start | stop }" >&2
    exit 1
    ;;

esac 