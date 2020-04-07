#!/bin/sh

set -xeuo pipefail

sudo apt-add-repository ppa:brightbox/ruby-ng
sudo apt-get update
sudo apt-get install ruby2.4

git clone git://github.com/imathis/octopress.git octopress
cd octopress
gem install bundler
rbenv rehash    # If you use rbenv, rehash to be able to run the bundle command
bundle install

rake install
sudo rake generate
