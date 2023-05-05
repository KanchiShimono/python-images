# python-images

This repository contains Ubuntu based Python container images, including CUDA images.

## Usage

The following examples show how to use the images. Replace the Python and CUDA versions with the ones you want to use.

CPU

```sh
docker pull kanchishimono/python:3.10-jammy
```

GPU (CUDA)

```sh
docker pull kanchishimono/python:3.10-cuda-11.8.0-cudnn8-devel-ubuntu22.04
```

## Why not [Docker official images](https://github.com/docker-library/python) or [Conda official images](https://github.com/ContinuumIO/docker-images)

Docker and Conda official images only provide Debian based images, and Ubuntu based images are not available.

There are several reasons why we might want to use Ubuntu images:

- Ubuntu's apt packages are updated more frequently and are better for using relatively newer tools
- Faster container vulnerability fixes
- Running machine learning with CUDA
- [There are no plans to support Ubuntu based images](https://github.com/docker-library/python/issues/61#issuecomment-282450114) in the official repository.

## Contributing

### Updating Dockerfile templates

The Dockerfiles in this repository are based on the files from the Docker official repository.
The differences from the official repository are stored in the [patches](./patches) folder.
When updating a file, please fetch the new version of the file from the official repository, edit it, and create a patch file for version control.

```sh
wget https://raw.githubusercontent.com/docker-library/python/331890ef059fae05f84c652520b78c340526dc71/Dockerfile-linux.template
git add Dockerfile-linux.template
# edit
# vim Dockerfile-linux.template
git diff Dockerfile-linux.template > patches/Dockerfile-linux.template.patch
```

### Updating Python versions

The versions specified in `versions.sh` will be written to `versions.json`.
List all the versions you want to build as arguments in `versions.sh`.
Versions not passed as arguments will be removed from `versions.json`.

```sh
./versions.sh 3.7 3.8 3.9 3.10 3.11
```

### Updating base images

Update the base images listed in `versions.sh`.
To add an entirely new image, update the FROM clause in `Dockerfile-linux.template`.

### Generating Dockerfiles

```sh
./apply-templates.sh
```
