# GeoMat _digital_ API

[![Build Status](https://travis-ci.org/GeoMatDigital/django-geomat.svg?branch=develop)](https://travis-ci.org/GeoMatDigital/django-geomat) [![codecov](https://codecov.io/gh/GeoMatDigital/django-geomat/branch/develop/graph/badge.svg)](https://codecov.io/gh/GeoMatDigital/django-geomat/branch/develop)

## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Maintainers](#maintainers)
- [Contribute](#contribute)
- [License](#license)

## Background

_WIP._

## Install

This project uses [docker-compose](https://docs.docker.com/compose/) and [pipenv](https://docs.pipenv.org). Go check them out if you don't have them locally installed.

To get started run `make`, which will pull all dependencies and build the Docker container.

```sh
$ make build
```

## Usage

To start the system, run:

```sh
$ docker-compose up -d
```

The API is now available on [http://localhost:8000](http://localhost:8000).

## Maintainers

- [@chgad](https://github.com/chgad)
- [@mimischi](https://github.com/mimischi)

## Contribute

Feel free to dive in! [Open an issue](https://github.com/GeoMatDigital/django-geomat/issues/new) or submit PRs.

## License

[BSD 3](LICENSE) © Michael Gecht
