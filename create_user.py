#!/usr/bin/python3
import os
import json
import sys

def read_files(filename: str):
    if not (os.path.exists("config.json")):
        sys.exit("You don't have config.json file!!")
    
    users_dict = {"users": []}

    with open('config.json', 'r') as config:
        configurations = json.load(config)

    with open('users.txt', 'r') as users:
        users_list = [line.rstrip('\n') for line in users]

    for user in users_list:
        username, password = user.split()
        users_dict['users'].append({
            "username": username,
            "password": password
        })
    
    return configurations, users_dict

def create_user(configs: dict, users: dict):
    for user in users['users']:
        stderr_create_user = os.system(
            f"""echo 'jenkins.model.Jenkins.instance.securityRealm.createAccount("{user['username']}", "{user['password']}")' | java -jar ./jenkins-cli.jar -s "{configs['jenkinsUrl']}" -auth {configs['adminUsername']}:{configs['adminUserPassword']} -noKeyAuth groovy = –"""
            )
        if(stderr_create_user != 0):
            print(f"Cannot create user: {user['username']}")

if(__name__ == "__main__"):
    filename = input("########################################################\n###  ~ Please run this script on your jenkins master !!!\n########################################################\nPlease enter your users text file name: ")
    configs, users = read_files(filename)
    if not (os.path.exists("jenkins-cli.jar")):
        stderr = os.system(f"curl {configs['jenkinsUrl']}/jnlpJars/jenkins-cli.jar -o jenkins-cli.jar")
        if(stderr != 0):
                print(f"Cannot get jenkins-cli.jar with curl command!")
    create_user(configs, users)
