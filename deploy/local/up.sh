#!/usr/bin/env bash

#
# Copyright (c) Dell Inc., or its subsidiaries. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#

set -ex
ROOT_DIR=$(readlink -f $(dirname $0))
cd ${ROOT_DIR}
export HOST_IP=${HOST_IP:-172.28.1.1}
export PRAVEGA_LTS_PATH=${PRAVEGA_LTS_PATH:-/tmp/pravega-lts}
docker-compose down -v

if ! [ -z "${PRAVEGA_LTS_PATH}" ]
then
   sudo rm -rf ${PRAVEGA_LTS_PATH}
fi

docker-compose up -d
#sleep 20s
#curl -X POST -H "Content-Type: application/json" -d '{"scopeName":"examples"}' http://localhost:10080/v1/scopes
#docker-compose logs --follow
