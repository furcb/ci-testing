#!/bin/env bash

## Vars
div="==="

## Check that code conforms to pep8 and passes linter
echo -e "$div Testing code style $div\n"
pycodestyle	testing/

echo -e "\n$div Running Linter on code $div\n"
pylint testing/

## Run unit and integration tests
echo -e "\n$div Running Tests $div\n"
python -m unittest
