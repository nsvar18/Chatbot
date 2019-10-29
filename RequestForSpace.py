# Natural Language Toolkit: Eliza
#
# Copyright (C) 2001-2017 NLTK Project
# Authors: Steven Bird <stevenbird1@gmail.com>
#          Edward Loper <edloper@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

# Based on an Eliza implementation by Joe Strout <joe@strout.net>,
# Jeff Epler <jepler@inetnebr.com> and Jez Higgins <mailto:jez@jezuk.co.uk>.

# a translation table used to convert things you say into things the
# computer says back, e.g. "I am" --> "you are"

from __future__ import print_function
from nltk.chat.util import Chat, reflections

# a table of response pairs, where each pair consists of a
# regular expression, and a list of possible responses,
# with group-macros labelled as %1, %2.

pairs = (

  (r'.*student union.*',
  ( "Sure, I can help you with it. Could you tell me when is the event? Please tell the date in mm/dd/yy format",
    "Sure, I can help you with the form submission. Could you tell me when is the event? Please tell the date in mm/dd/yy format",
    "Sure, I can help you with form submission. Just for your information submitting a form does not guarantee event space. It all depends on Availability.")),

  (r'Ok(.*)',
  ( "Great. So when is the event, could you please tell me the date in mm/dd/yy format?",
    "What is the date for which you want to reserve event space?please tell me the date in mm/dd/yy format")),

  (r'.*?[0-9]*\/[0-9]*\/[0-9]*',
  ( "Great! Could you please tell me event's name?",
    "what is the event?")),

  (r'.*event.*?is.*',
  ( "Oh nice. What is the expected attendance count?",
    "Could you please tell the expected count of people attending the event")),

  (r'.*?expected [attendance|count]* is [0-9]*',
  ( "Ok. Could you also tell the start and end time of the event. Please answer time in AM/PM format",
    "for what time of the day do you want the event space? We need the start and end time for the event.")),

  (r'.*?[begin|start].*[AM|PM].*',
  ( "Ok and what is the event for? Is it a Banquet or a lecture or a concert or a conference or exposition or film screening or dance/party or a reception?Please answer from one of these options",
    "What is the activity that event refers too?  Is it a Banquet or a lecture or a concert or a conference or exposition or film screening or dance/party or a reception?Please answer from one of these options",)),

  (r'[Banquet|Lecture|concert|confererence|exposition|Film\s*screening|Dance|Party|Reception]',
  ( "Great!",
    "Would you prefer it if I were not %1?",
    "Perhaps you believe I am %1.",
    "I may be %1 -- what do you think?")),

  (r'What (.*)',
  ( "Why do you ask?",
    "How would an answer to that help you?",
    "What do you think?")),

  (r'How (.*)',
  ( "How do you suppose?",
    "Perhaps you can answer your own question.",
    "What is it you're really asking?")),

  (r'Because (.*)',
  ( "Is that the real reason?",
    "What other reasons come to mind?",
    "Does that reason apply to anything else?",
    "If %1, what else must be true?")),

  (r'(.*) sorry (.*)',
  ( "There are many times when no apology is needed.",
    "What feelings do you have when you apologize?")),

  (r'[Hello|Hi]*(.*)',
  ( "Hello..How can I help you today?",
    "Hi there... how are you?",)),

  (r'I think (.*)',
  ( "Do you doubt %1?",
    "Do you really think so?",
    "But you're not sure %1?")),

  (r'(.*) friend (.*)',
  ( "Tell me more about your friends.",
    "When you think of a friend, what comes to mind?",
    "Why don't you tell me about a childhood friend?")),

  (r'Yes',
  ( "You seem quite sure.",
    "OK, but can you elaborate a bit?")),


  (r'Is it (.*)',
  ( "Do you think it is %1?",
    "Perhaps it's %1 -- what do you think?",
    "If it were %1, what would you do?",
    "It could well be that %1.")),

  (r'It is (.*)',
  ( "You seem very certain.",
    "If I told you that it probably isn't %1, what would you feel?")),

  (r'Can you (.*)',
  ( "No I can not. You have to choose appropriately",
    "Why do you ask if I can %1?")),

  (r'Can I (.*)',
  ( "Yes you can",
    "Do you want to be able to %1?")),

  (r'quit',
  ( "Thank you for talking with me.",
    "Good-bye."))
)

eliza_chatbot = Chat(pairs, reflections)

def eliza_chat():
    print("Therapist\n---------")
    print("Talk to the program by typing in plain English, using normal upper-")
    print('and lower-case letters and punctuation.  Enter "quit" when done.')
    print('='*72)
    print("Hello.  How can I help you?")

    eliza_chatbot.converse()

def demo():

    eliza_chat()

if __name__ == "__main__":
    demo()

