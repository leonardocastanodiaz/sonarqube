#!/usr/bin/python
import os, json, csv
from sonarqube import SonarQubeClient
from dotenv import load_dotenv
load_dotenv()
token=os.environ.get('token')
user=os.environ.get('user')
passwd=os.environ.get('passwd')
url=os.environ.get('url')
projects_db=['project1key','project2key','project3key']
sonar = SonarQubeClient(sonarqube_url=url, username=user, password=passwd)
def get_main_branch_name(project_key):
    branches = sonar.project_branches.search_project_branches(project=project_key)
    for branch in branches["branches"]:
        if branch['isMain']:
            print(f"Project Name: {project_key}, is Main: {branch['isMain']}, Branch Name: {branch['name']}")
      

def get_projects_names():
    components = sonar.projects.search_projects()
    for component in components["components"]:
        get_main_branch_name(component["key"])
get_projects_names()    
