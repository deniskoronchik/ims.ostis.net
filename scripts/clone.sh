#!/bin/bash

. ./common.sh --source-only

stage "Clone projects"

clone_project https://github.com/deniskoronchik/sc-machine.git sc-machine master
clone_project https://github.com/deniskoronchik/sc-web.git sc-web master
clone_project https://github.com/deniskoronchik/ims.ostis.kb.git ims.ostis.kb master
