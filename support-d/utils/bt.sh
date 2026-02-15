gdb /usr/local/fluxpbx/bin/fluxpbx $1 \
        --eval-command='set pagination off' \
        --eval-command='thread apply all bt' \
        --eval-command='quit'
