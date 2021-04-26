#!/bin/sh

# docker pull ubuntu:latest

#docker build -t pico .

docker run -v "~/git/ctf-writeups/picoCTF-2018":/mnt/pico -i -t --name pico --cap-add=SYS_PTRACE --entrypoint /bin/bash ubuntu:latest 
# -v mounts [local]/[remote] paths
# -i keeps the container running after detach
# -t displays the pash terminal into our main terminal
# --name sets the name of the container
# --cap-add: Add Linux capabilities
# --entrypoint /bin/bash sets the entry point to the bash terminal
