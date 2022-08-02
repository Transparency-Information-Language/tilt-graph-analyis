from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from pkg_resources import ContextualVersionConflict

# from rich.console import Console

import requests
import json

import time
from sqlalchemy import delete
from tqdm import tqdm

# console = Console()

sample_transport=RequestsHTTPTransport(
    url='http://localhost:4001/graphql',
    use_json=True,
    headers={
        "Content-type": "application/json",
    },
    verify=False
)

client = Client(
    #execute_timeout=20,
    transport=sample_transport,
    fetch_schema_from_transport=True,
)

session = requests.Session()
session.auth = ('admin', "secret")

hostname = 'http://ec2-3-64-237-95.eu-central-1.compute.amazonaws.com:8080/tilt/tilt'
auth = session.post(hostname)
response = json.loads(session.get(hostname).content)

#tilt = json.loads(requests.get('http://ec2-3-64-237-95.eu-central-1.compute.amazonaws.com:8080/tilt/tilt').content)
#print("Fetch Successful!", response)


json_file = open('/Users/johannes/Desktop/TU/playground/tilt')
tilt = json.load(json_file)

print('Purposes:')


tilt_nodes = []
tilt_edges = []

"""for i in tilt:
    #print(i)
    #record node
    tilt_nodes.append([str.lower(i['meta']['name']), str.lower(i['meta']['url'])])

    #loop through outgoing data
    for e in i['dataDisclosed']:

        #loop through recipients
        for r in e['recipients']:
        #record the egde
            #print(e['purposes'][0]['purpose'])

            try:
                if r['name'] != [] and len(r['name'])<100:
                    tilt_edges.append([str.lower(i['meta']['name']), str.lower(r['name']), str.lower(e['purposes'][0]['purpose'])])

                    if str.lower(r['name']) not in tilt_nodes:
                        tilt_nodes.append([str.lower(r['name']), ''])
            except:
                continue

        print(i['meta']['name'])

        query_string = "mutation {createDataProtectionOfficers(input: { name: \""+i['meta']['name']+"\"}) {dataProtectionOfficers {name}}}"
        query = gql(query_string)
        client_response = client.execute(query)
        print(client_response)


for i in tqdm(range(1, len(purposes) + 1)):
    p = purposes['%s' % (i)]
    description = p['description'].replace('"', '\\"').replace(':', '\:"')
    descriptionLegal = p['descriptionLegal'].replace('"', '\\"').replace('\n', '')
    query_string = 'mutation { CreatePurpose(id: %s, name: "%s", description: "%s", descriptionLegal: "%s") { _id }}' % (p['id'], p['name'], description, descriptionLegal)
    print("Query String: ", query_string)
    query = gql(query_string)
    client.execute(query)
    i = i + 1
"""
