#!/usr/bin/env bash

echo 'Install selenium'
pip3 install -U selenium
echo 'Install PhantomJS'
npm -g install phantomjs-prebuilt

python3 ./src/main.py