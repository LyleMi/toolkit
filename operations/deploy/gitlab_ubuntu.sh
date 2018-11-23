#!/bin/sh

# source: https://about.gitlab.com/installation/#ubuntu
# date: 2018-05-02

# Install and configure the necessary dependencies 
sudo apt-get update
sudo apt-get install -y curl openssh-server ca-certificates
sudo apt-get install -y postfix

# Add the GitLab package repository and install the package 
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh | sudo bash
sudo EXTERNAL_URL="http://gitlab.example.com" apt-get install gitlab-ee
