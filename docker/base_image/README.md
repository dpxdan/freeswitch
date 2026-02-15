About
-----

This is minimized official FluxPbx docker container.
Container designed to run on host network.
Size of container decreased to 120MB (54MB compressed)
Significantly increased security:
1) removed all libs except libc, busybox, fluxpbx and dependent libs.
2) removed 'system' API command from vanila config
3) updated FluxPbx default SIP password to random value

Used environment variables
--------------------------

1) ```SOUND_RATES``` - rates of sound files that must be downloaded and installed. Available values ```8000```, ```16000```, ```32000```, ```48000```. May defined multiply values using semicolon as delimiter. Example ```SOUND_RATES=8000:16000```;
2) ```SOUND_TYPES``` - types of sound files that must be downloaded and installed. Available values music, ```pt-BR-karina```, ```en-us-allison```, ```ru-RU-elena```, ```en-ca-june```, ```fr-ca-june```, ```pt-BR-karina```, ```sv-se-jakob```, ```zh-cn-sinmei```, ```zh-hk-sinmei```. Example ```SOUND_TYPES=music:pt-BR-karina```;
3) ```EPMD``` - start epmd daemon, useful when you use mod_erlang and mod_kazoo FluxPbx modules. Available values ```true```, ```false```.

Usage container
---------------

1) Creating volume for sound files. This may be skipped if you not use fluxpbx MOH and other sound files.
```sh
docker volume create --name fluxpbx-sounds 
```

2) Stating container
```sh
docker run --net=host --name fluxpbx \
           -e SOUND_RATES=8000:16000 \
           -e SOUND_TYPES=music:pt-BR-karina \
           -v fluxpbx-sounds:/usr/share/fluxpbx/sounds \
           -v /etc/fluxpbx/:/etc/fluxpbx \
           safarov/fluxpbx
```

systemd unit file
-----------------
You can use this systemd unit file on your hosts.
```sh
$ cat /etc/systemd/system/fluxpbx-docker.service
[Unit]
Description=fluxpbx Container
After=docker.service network-online.target
Requires=docker.service


[Service]
Restart=always
TimeoutStartSec=0
#One ExecStart/ExecStop line to prevent hitting bugs in certain systemd versions
ExecStart=/bin/sh -c 'docker rm -f fluxpbx; \
          docker run -t --net=host --name fluxpbx \
                 -e SOUND_RATES=8000:16000 \
                 -e SOUND_TYPES=music:pt-BR-karina \
                 -v fluxpbx-sounds:/usr/share/fluxpbx/sounds \
                 -v /etc/kazoo/fluxpbx/:/etc/fluxpbx \
                 fluxpbx'
ExecStop=-/bin/sh -c '/usr/bin/docker stop fluxpbx; \
          /usr/bin/docker rm -f fluxpbx;'

[Install]
WantedBy=multi-user.target
```
Unit file can be placed to ```/etc/systemd/system/fluxpbx-docker.service``` and enabled by command
```sh
systemd start fluxpbx-docker.service
systemd enable fluxpbx-docker.service
```

.bashrc file
------------
To simplify fluxpbx management you can add alias for ```fs_cli``` to ```.bashrc``` file as example bellow.
```sh
alias fs_cli='docker exec -i -t fluxpbx /usr/bin/fs_cli'
```

How to create custom container
------------------------------
This container created from scratch image by addiding required fluxpbx files packaged to tar.gz archive.
To create custom container:
1) install required FluxPbx packages. Now supported debian dist
```sh
apt-get install fluxpbx-conf-vanilla
```
2) clone fluxpbx repo
```sh
git clone https://github.com/signalwire/fluxpbx.git
```
3) execute ```make_min_archive.sh``` script
```sh
cd fluxpbx/docker/base_image
./make_min_archive.sh
```
4) build custom container
```sh
docker build -t fluxpbx_custom .
```

Read more
---------

[Dockerfile of official FluxPbx container](https://github.com/signalwire/fluxpbx/tree/master/docker/release)
