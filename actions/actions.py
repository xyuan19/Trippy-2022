from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet, FollowupAction
import requests
import random
import re

from dotenv import dotenv_values

config = dotenv_values(".env")
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class LoginOrRegister(Action):

    def name(self) -> Text:
        return "action_sign_in_or_up"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="I need to know your user account to proceed, do you want to login with existing account or register a new one?",
            buttons= [
                {"payload": f"sign in", "title": "Sign in"},
                {"payload": f"sign up", "title": "Sign up"},
            ]
        )
        sign_in_or_up = tracker.get_intent_of_latest_message()
        return [SlotSet("sign_in_or_up", sign_in_or_up)]

#
# class Register(Action):
#     def name(self) -> Text:
#         return "action_register"
#
#     async def run(
#             self,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         username = tracker.get_slot("username")
#         password = tracker.get_slot("password")
#         r = requests.post(f'{config["DB_API_ADDRESS"]}/user/register',
#                           json={
#                               "username": username,
#                               "password": password
#                           })
#         if r.status_code == requests.codes.created:
#             dispatcher.utter_message(f"Hi {username}")
#             last_intent = tracker.get_slot("last_intent")
#             destination = tracker.get_slot("destination")
#
#             evts = [SlotSet("is_authenticated", True)]
#             return evts
#
#         else:
#             dispatcher.utter_message(
#                 f"There is something wrong during the process please contact Trippy if you need more information")
#             return [
#                 SlotSet("is_authenticated", False),
#                 SlotSet("username", None),
#                 SlotSet("password", None),
#             ]