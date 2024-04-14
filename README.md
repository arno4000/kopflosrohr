# kopflosrohr
Containerized headless YouTube TV for receiving YouTube Audio Streams.

For now, build the container with `docker build . -t <name-of-the-image>`. I will push an image soon.

You have to have `pulseaudio` installed on your server and be able to play audio. This can be testet using the command `aplay /usr/share/sounds/alsa/Front_Right.wav`. `alsa-utils` is required for the aplay command.

Docker Compose file:
```yaml
services:
    docker-chromium:
        environment:
            - PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native
        volumes:
            - ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native
            - ~/.config/pulse/cookie:/root/.config/pulse/cookie
        devices:
            - /dev/snd:/dev/snd
        stdin_open: true
        tty: true
        image: phonkd/kopflosrohr:0.1 # or phonkd/kopflosrohr:0.1-arm64 if you want to use tha arm64 image
```
