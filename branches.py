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
    #for key, value in branches.items():
      #print(f'{key},{value}')
    for branch in branches["branches"]:
        if branch['isMain']:
            print(f"Project Name: {project_key}, is Main: {branch['isMain']}, Branch Name: {branch['name']}")
      

def get_projects_names():
    components = sonar.projects.search_projects()
   # for component in components:
    #    print(f"{components.get('key')}")
    for component in components["components"]:
        get_main_branch_name(component["key"])
            #print(f"Component: {component['key']}")
        #projectkey = project['key']
    #get_main_branch_name(projectkey)
# components [{'key': 'project1key', 'name': 'project1', 'qualifier': 'TRK', 'visibility': 'public'}, {'key': 'project2key', 'name': 'project2', 'qualifier': 'TRK', 'visibility': 'public'}, {'key': 'project3key', 'name': 'project3', 'qualifier': 'TRK', 'visibility': 'public'}]
get_projects_names()    
#get_main_branch_name('')
