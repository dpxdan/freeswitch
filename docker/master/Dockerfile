# vim:set ft=dockerfile:
ARG DEBIAN_VERSION=bookworm
FROM debian:${DEBIAN_VERSION}

# ARGs are cleared after every FROM
# see: https://docs.docker.com/engine/reference/builder/#understand-how-arg-and-from-interact
ARG DEBIAN_VERSION
ARG TOKEN

# By default, install the full set of FluxPBX packages.  Specify an alternative with:
#   --build-arg="FS_META_PACKAGE=fluxpbx-meta-vanilla"
# alternatives include:
#   fluxpbx-meta-bare
#   fluxpbx-meta-vanilla
#   fluxpbx-meta-sorbet
#   fluxpbx-meta-all-dbg
ARG FS_META_PACKAGE=fluxpbx-meta-all

# Source Dockerfile:
# https://github.com/docker-library/postgres/blob/master/9.4/Dockerfile

# explicitly set user/group IDs
ARG FLUXPBX_UID=499
ARG FLUXPBX_GID=499
RUN groupadd -r fluxpbx --gid=${FLUXPBX_GID} && useradd -r -g fluxpbx --uid=${FLUXPBX_UID} fluxpbx

# make the "en_US.UTF-8" locale so fluxpbx will be utf-8 enabled by default
RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends ca-certificates gnupg2 gosu locales wget \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

# https://fluxpbx.org/confluence/display/FLUXPBX/Debian
# https://developer.signalwire.com/fluxpbx/FluxPBX-Explained/Installation/Linux/Debian_67240088/

RUN wget --no-verbose --http-user=signalwire --http-password=${TOKEN} \
      -O /usr/share/keyrings/signalwire-fluxpbx-repo.gpg \
      https://fluxpbx.signalwire.com/repo/deb/debian-release/signalwire-fluxpbx-repo.gpg \
    && echo "machine fluxpbx.signalwire.com login signalwire password ${TOKEN}" > /etc/apt/auth.conf \
    && echo "deb [signed-by=/usr/share/keyrings/signalwire-fluxpbx-repo.gpg] https://fluxpbx.signalwire.com/repo/deb/debian-release/ ${DEBIAN_VERSION} main" > /etc/apt/sources.list.d/fluxpbx.list \
    && apt-get -qq update \
    && apt-get install -y ${FS_META_PACKAGE} \
    && apt-get purge -y --auto-remove \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY docker-entrypoint.sh /
# Add anything else here

## Ports
# Document ports used by this container
### 8021 fs_cli, 5060 5061 5080 5081 sip and sips, 5066 ws, 7443 wss, 8081 8082 verto, 16384-32768, 64535-65535 rtp
EXPOSE 8021/tcp
EXPOSE 5060/tcp 5060/udp 5080/tcp 5080/udp
EXPOSE 5061/tcp 5061/udp 5081/tcp 5081/udp
EXPOSE 5066/tcp
EXPOSE 7443/tcp
EXPOSE 8081/tcp 8082/tcp
EXPOSE 64535-65535/udp
EXPOSE 16384-32768/udp

# Volumes
## Fluxpbx Configuration
VOLUME ["/etc/fluxpbx"]
## Tmp so we can get core dumps out
VOLUME ["/tmp"]

# Limits Configuration
COPY    build/fluxpbx.limits.conf /etc/security/limits.d/

# Healthcheck to make sure the service is running
SHELL       ["/bin/bash", "-c"]
HEALTHCHECK --interval=15s --timeout=5s \
    CMD  fs_cli -x status | grep -q ^UP || exit 1

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["fluxpbx"]
