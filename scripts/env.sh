#!/bin/bash

. ./common.sh --sources-only

cd ..

stage "Configure virtual environment"
sudo apt-get install python-pip python-dev build-essential
sudo pip install --upgrade pip
sudo pip install --upgrade virtualenv

substage "Create"
virtualenv --prompt="ims.env" ./env

mkdir ./logs
mkdir ./pids

substage "Install dependecies"
source ./env/bin/activate
export PIP_REQUIRE_VIRTUALEV=true
./env/bin/pip install --requirement=./config/packages.conf --log=./logs/build_pip_packages.log

substage "Relocatable"
virtualenv --relocatable ./env

cd -
