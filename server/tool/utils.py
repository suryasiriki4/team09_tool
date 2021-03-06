"""
some of the utility links and data structures required in the tool.py
"""

from collections import namedtuple

BASE_URL = "https://api.stackexchange.com/2.2"
SEARCH_URL = BASE_URL + "/search?site=stackoverflow"
ANSWERS_URL = BASE_URL + "/questions/<id>/answers?site=stackoverflow" + "&filter=withbody" + "&order=desc" + "&sort=votes"
QUESTIONS_URL = BASE_URL + "/questions/<id>?site=stackoverflow" + "&filter=withbody"

# namedtuples to represent simple objects
Question = namedtuple("Question", ["id", "has_accepted", "body", "url"])
Answer = namedtuple("Answer", ["id", "accepted", "score", "body", "author", "profile_image"])