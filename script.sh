#! /bin/bash

## -----install python interpreters using pyenv-----
# install python 2.7.0 version using pyenv
pyenv install 2.7.0

# install python 3.7.0 version using pyenv
pyenv install 3.7.0

## -----create 2 virtualenv environments-----
# create virtual environment with 2.7.0 version of python
pyenv virtualenv 2.7.0 firstproject

# create virtual environment with 3.7.0 version of python
pyenv virtualenv 3.7.0 secondproject