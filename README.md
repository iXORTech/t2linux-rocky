# t2linux-rocky-kernel

Patched kernel and supporting packages for hardware enablement on T2 macs. <!--Binary packages are available from [copr](https://copr.fedorainfracloud.org/coprs/sharpenedblade/t2linux). You can also download and install the `copr-sharpenedblade-t2linux-release` package.--> Forked from the official [T2Linux Fedora kernel patch and packages](https://github.com/t2linux/fedora).

The internal ssd, camera, mic, and the keyboard/trackpad work out of the box. WiFi and Bluetooth might work with some extra steps. Read [the wiki](https://wiki.t2linux.org/state/) for information about the latest hardware support.

This kernel is usually at the same version as the stable Rocky Linux kernel. It is currently built for Rocky Linux 10.

## Instalation

<!-- Download the live ISO from [here](https://github.com/t2linux/fedora-iso). Follow the [installation guide](https://wiki.t2linux.org/distributions/fedora/installation/).-->

_TODO_

## WiFi/Bluetooth

Follow the [firmware guide](https://wiki.t2linux.org/guides/wifi/).

## Building from source

Clone this repo locally:

```bash
git clone --recursive --depth 1 https://github.com/iXORTech/t2linux-rocky
cd t2linux-rocky
```

Then run the build container, which has dependencies already installed. The packages will be in `builddir`. If you want to only build a specific package, pass its name as a argument to this command:

```bash
podman run --privileged -v "$PWD":/repo ghcr.io/ixortech/rocky-ci:unstable /repo/build-packages.sh
```

## Credits

This kernel was heavily inspired by [mikeeq/mbp-fedora-kernel](https://github.com/mikeeq/mbp-fedora-kernel). The patches are from the [t2linux](https://t2linux.org) project and created by [everyone that contributed to to it](https://github.com/t2linux/linux-t2-patches/graphs/contributors).

## Disclaimer

This project is not officially provided or supported by Rocky Linux and the T2 Linux Project. The official Rocky Linux software is available at [https://rockylinux.org/](https://rockylinux.org/). This project is not related to Rocky Linux in any way.
