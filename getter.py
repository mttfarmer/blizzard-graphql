import requests, util, constants, os
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

def getD3Acts():
    bliz = util.getAuthorisedClient(os.environ["Blizzard_Client_Id"], os.environ["Blizzard_Client_Secret"])
    return bliz.get(constants.baseUrl + "d3/data/act?locale=en_US").json()