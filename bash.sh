#!/bin/bash

sudo apt update -y >/dev/null 2>&1
sudo apt install tor proxychains -y >/dev/null 2>&1

nohup tor >/dev/null 2>&1 &
