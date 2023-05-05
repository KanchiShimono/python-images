#!/usr/bin/env bash
# https://raw.githubusercontent.com/docker-library/python/c484e1ba82213c6a2e8785342630e5383d943d02/update.sh
set -Eeuo pipefail

cd "$(dirname "$(readlink -f "$BASH_SOURCE")")"

./versions.sh "$@"
./apply-templates.sh "$@"
