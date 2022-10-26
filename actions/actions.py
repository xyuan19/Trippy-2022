from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet, FollowupAction
import requests
import random
import re
from trippy_db_utils import *

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


class Sign_in(Action):
    def name(self) -> Text:
        return "action_sign_in"

    # get username, password
    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        username = tracker.get_slot("username")
        password = tracker.get_slot("password")

        # connected to db, check user's information
        # print(check_user_information(username,password))
        if check_user_information(username, password):
            dispatcher.utter_message(f"Hi {username}")
            dispatcher.utter_message(response="utter_show_menu")
        else:
            dispatcher.utter_message(f"sorry, The user name or password is incorrect.\nYou can try again or sign in by tester's account:\n\t username: test\n\t password: 123456test")
            dispatcher.utter_message(response="sign_in_form")
            return [
                SlotSet("login_or_not", False),
                SlotSet("username", None),
                SlotSet("password", None)
            ]


class Sign_up(Action):
    def name(self) -> Text:
        return "action_sign_up"

    # get username, password
    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        username = tracker.get_slot("username")
        password = tracker.get_slot("password")

        # connected to db, add user's information
        add_user_information(username,password)

        # given back
        if check_user_information(username, password):
            dispatcher.utter_message(f"Hi {username}")
            dispatcher.utter_message(response="utter_show_menu")
        else:
            dispatcher.utter_message(f"sorry, The name or password is incorrect."
                                     f"\nYou can try again to sign up.")
            dispatcher.utter_message(response="sign_up_form")
            return [
                SlotSet("login_or_not", False),
                SlotSet("username", None),
                SlotSet("password", None)
            ]
