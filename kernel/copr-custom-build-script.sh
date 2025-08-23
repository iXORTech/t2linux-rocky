#!/usr/bin/bash

git clone --recurse-submodules https://github.com/iXORTech/t2linux-rocky
cd t2linux-rocky/kernel
export package_builddir="$PWD"
./kernel.sh
