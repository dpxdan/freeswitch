#!/bin/bash
set -e

# Source docker-entrypoint.sh:
# https://github.com/docker-library/postgres/blob/master/9.4/docker-entrypoint.sh
# https://github.com/kovalyshyn/docker-fluxpbx/blob/vanilla/docker-entrypoint.sh

if [ "$1" = 'fluxpbx' ]; then

    if [ ! -f "/etc/fluxpbx/fluxpbx.xml" ]; then
        mkdir -p /etc/fluxpbx
        cp -varf /usr/share/fluxpbx/conf/vanilla/* /etc/fluxpbx/
    fi

    chown -R fluxpbx:fluxpbx /etc/fluxpbx
    chown -R fluxpbx:fluxpbx /var/{run,lib}/fluxpbx
    
    if [ -d /docker-entrypoint.d ]; then
        for f in /docker-entrypoint.d/*.sh; do
            [ -f "$f" ] && . "$f"
        done
    fi
    
    exec gosu fluxpbx /usr/bin/fluxpbx -u fluxpbx -g fluxpbx -nonat -c
fi

exec "$@"
