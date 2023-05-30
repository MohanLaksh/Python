# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 14:26:11 2023

@author: 01001X744
"""

# coding: utf-8
from dataclasses import dataclass, asdict, field
from typing import Dict, List, Optional
import pprint
import json
import pandas as pd
try:
  import requests
except ImportError:
  raise SystemExit("Please install 'requests' first")

@dataclass
class Note:
    Title: str
    Type: int
    Ordinal: str
    Value: str

@dataclass
class Vulnerability:
    Title: Dict
    Notes: List[Note]
    DiscoveryDateSpecified: bool 
    ReleaseDateSpecified: bool
    Ordinal: str
    RevisionHistory: List[Dict]
    CVE: str 
    ProductStatuses: List[Dict]
    Threats: List[Dict]
    CVSSScoreSets: List
    Remediations: List
    Acknowledgments: List



@dataclass(init=False)
class CVRF:
    DocumentTitle: str
    DocumentType: str
    DocumentPublisher : Dict[str, Dict]
    DocumentTracking: Dict[str, Dict]
    DocumentNotes: List[Dict]
    ProductTree: Dict
    Vulnerabilities: List[Vulnerability]

    @classmethod
    def init(cls, raw):
        obj = cls()
        obj.DocumentTitle = raw.get("DocumentTitle").get("Value")
        obj.DocumentType = raw.get("DocumentType").get("Value")
        obj.DocumentPublisher = raw.get("DcoumentPublisher")
        obj.DocumentTracking = raw.get("DcoumentTracking")
        obj.DocumentNotes = raw.get("DcoumentNotes")
        obj.ProductTree = raw.get("ProductTree")
        obj.Vulnerabilities = []
        for vuln in raw.get("Vulnerability", []):
            pprint.pprint(vuln)
            obj.Vulnerabilities.append(Vulnerability(**vuln))

        return obj


    def is_security(self) -> bool:
        if self.DocuemntType['Value'] == 'Security Update':
            return True
        return False
    
    def Affected(self) -> List[str]:
        values = set()
        for item in self.ProductTree['Branch']['Items']:
            for product in item['Items']:
                values.add(product['Value'])
        return list(values)


@dataclass
class SecurityUpdate:
    ID: str
    Alias: str = field(repr=False)
    DocumentTitle: str
    Severity: str
    InitialReleaseDate: str = field(repr=False)
    CurrentReleaseDate: str
    CvrfUrl: str = field(repr=False)
    Cvrf: CVRF = field(repr=False, default=None)

    def summary(self):
        return f"{self.DocumentTitle}({self.ID}): {len(self.Cvrf.Vulnerability)}"

    def dump(self, filename: str=None):
        if filename is None:
            filename = f"{self.ID}_Security_Update.json"
        data = {
            'ID': self.ID,
            'title': self.DocumentTitle,
            'ReleaseDate': self.CurrentReleaseDate,
        }
        if self.Cvrf:
            data['cvrf'] = asdict(self.Cvrf)
        with open(filename, 'w') as f:
           f.write(json.dumps(data, indent=2))


url = 'https://api.msrc.microsoft.com'
key = 'MSRC_API_KEY'
headers = {
    'Accept': 'application/json',
    'api-key': key,
}
params = {'api-version': 2020}
updates_query = f"{url}/updates"
r = requests.get(updates_query, headers=headers, params=params)
if r.status_code != 200:
    raise SystemExit("Failed to get updates")
updates = [SecurityUpdate(**update) for update in r.json().get('value')]

for update in updates:
    while update.ID == "2023-Mar":
        r = requests.get(update.CvrfUrl, headers=headers, params=params)
        if r.status_code != 200:
            print(f"Failed to get update: {ID}")
            continue
        try:
            data = r.json()
            print(f"Init {update.ID}")
            cvrf = CVRF.init(data)
            update.Cvrf = cvrf
            #print(f"{update.summary()}")
            print(f"{update}")
            print(type(update))
            update.dump()
        except Exception as e:
            print(f"Failed to get CVRF: {update.ID} Error: {e}")
            raise(e)
        
data1 = pd.DataFrame.from_dict(data)

filname = "2016-Nov_Security_Update.json"
extract = pd.read_json("2016-Nov_Security_Update.json", lines=True, encoding = 'utf-8-sig')
import json
with open(filname, 'r') as datafile:
    data2 = json.load(datafile)
retail = pd.DataFrame(data2)
retail.columns
retail
pd.set_option('display.width', 1000)

import random
random.seed(19)
random.randint(1, 1000)
random.seed()