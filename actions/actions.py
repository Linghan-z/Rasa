
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from actions.api import question_parser
from actions.api import answer_search


class FindTheCorrespondingMilitary(Action):

    def name(self) -> Text:
        return "find_the_corresponding_military"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        military = tracker.get_slot('Military')
        intention = tracker.get_intent_of_latest_message()
        data = {'args': {military: ['Military']}, 'question_type': [intention]}
        parser = question_parser.QuestionPaser()
        searcher = answer_search.AnswerSearcher()
        sql = parser.parser_main(data)
        final_answer = searcher.search_main(sql)

        # dispatcher.utter_message(text="Hello World!")
        dispatcher.utter_message(final_answer)
        return []
