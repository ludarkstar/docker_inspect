# -*- coding: utf-8 -*-
##############################################################################################
# Citra IT
# Author: luciano@citrait.com.br
# Date: 20/03/2021 Version 1.0
# Script to parse "docker inspect" and retrieve importante information about a container
##############################################################################################
import sys
import subprocess
import json

if len(sys.argv) < 2:
    print("please, specify the container name!")

print("//////////////////////////////////////////////////////////////////////")
print(f" Container: {sys.argv[1]}")
print("//////////////////////////////////////////////////////////////////////")
p = subprocess.run(("/usr/bin/docker", "inspect", sys.argv[1]), stdout=subprocess.PIPE)


try:
    inspect_json = json.loads(p.stdout)[0]
except:
    print("Erro ao carregar arquivo json " + INSPECT_FILE)
    raise("Error loading input file!")

print("Container name: " + str(inspect_json['Name']))
print("Network: " + str(inspect_json['HostConfig']['NetworkMode']))
print("Image: " + str(inspect_json['Config']['Image']))
print("Command: " + str(inspect_json['Config']['Cmd']))

if inspect_json['Config']['Env'] is not None:
    print("Environments: ")
    for env in inspect_json['Config']['Env']:
        print("\t" + str(env))

if len(inspect_json['HostConfig']['PortBindings']) > 0:
    print("Ports: ")
    for port_keys in inspect_json['HostConfig']['PortBindings'].keys():
        for port in inspect_json['HostConfig']['PortBindings'][port_keys]:
            cport = port_keys.split("/")[0]
            print("\t" + port['HostPort'] + ":" + cport)

if inspect_json['HostConfig']['Binds'] is not None:
    print("Mounts: ")
    for bind in inspect_json['HostConfig']['Binds']:
        print("\t" + bind)
