#!/bin/bash

. ./common.sh --source-only

cd ../
source env/bin/activate
cd -

stage "Build projects"

substage "sc-machine"
cd ../sc-machine/scripts
./install_deps_ubuntu.sh

if [ ! -d "redis-2.8.4" ]; then
./install_redis_ubuntu.sh
fi

./clean_all.sh
./make_all.sh
cd -

substage "sc-web"
cd ../sc-web/scripts
./prepare_js.sh

python build_components.py -i -a
cd -

substage "sctp server configuration"
python sctp_conf.py ../config/sc-web.ini

substage "tornado server configuration"
python server_conf.py ../config/server.conf

substage "Build knowledge base"
./build_kb.sh

substage "services"
sudo python services.py $USER
sudo restart scweb
sudo restart sctp
