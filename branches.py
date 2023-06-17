#!/usr/bin/python
import os, json, csv
from sonarqube import SonarQubeClient
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get('token')
user = os.environ.get('user')
passwd = os.environ.get('passwd')
url = os.environ.get('url')
sonar = SonarQubeClient(sonarqube_url=url, username=user, password=passwd)



def store_file_csv(branches_list):
    headerList = ['Project', 'Branch']
    with open('branches.csv', 'w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for branch in branches_list:
            writer.writerows([[branch]])


def get_main_branch_name(projects_keys):
    branch_to_print = []
    branch_to_print.append("PROJECT_NAME, BRANCH_NAME")
    for project_key in projects_keys:
        branches = sonar.project_branches.search_project_branches(project=project_key)
        for branch in branches["branches"]:
            if branch['isMain']:
                branch_to_print.append(project_key+", "+branch['name'])
    store_file_csv(branch_to_print)

def get_projects_names():
    components = sonar.projects.search_projects()
    projects_keys = []
    for component in components["components"]:
        projects_keys.append(component["key"])
    get_main_branch_name(projects_keys)

get_projects_names()    
