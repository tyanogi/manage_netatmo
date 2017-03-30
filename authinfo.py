#!/usr/bin/python3
# encoding=utf-8

import lnetatmo

class set:
    def __init__(self):
        # NETATMOの認証情報を設定
        self.authorization = lnetatmo.ClientAuth(
                        clientId = "NETATMO Client id",
                        clientSecret = "NETATMO Client secret",
                        username = "NETATMO Username",
                        password = "NETATMO Password",
        )

        # ThingSpeakのWrite_API_Keyを設定
        self.apikey = "ThingSpeak Write API Key"

