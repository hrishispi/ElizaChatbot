#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 05:44:06 2021

@author: prakritipanday
"""
import re
import random
import nltk
from nltk.tokenize import word_tokenize

conversation_dict = {

    r'.*(kids?|child|children).*':
        [
            "Can you tell me more about your \1?",
            "How would you describe your relationship with your \1?",
            "What do you enjoy doing with your \1?"
        ],

    r'I lost (.*)':
        [
            "I'm sorry to hear that. Can you tell me what happened?",
            "That must be tought. How are you feeling now?",
            "How are you dealing with the loss of %s?"
        ],

    r'.*(depressed|sad|pressure|stress).*':
        [
            "Why do you feel \1?",
            "Have you talked to anyone about how you are feeling?",
            "How do you prefer managing feeling \1?"
        ],
    r'.*(kill|suicide|die).*':
        [
            "Please stop dwelling on such thoughts. Do you share these thoughts with others in your life?",
            "Would you like to call the National Suicide Prevention Lifeline at 1-800-273-8255 (Talk)? The toll-free confidential Lifeline is available 24 hours a day, seven days a week",
            "%s eliminates the possibility of improving the situation. Surely, we can find a solution"
        ],
    r'.*(job|work|career).*':
        [
            "Do you like what you do?",
            "Can you tell me more about your \1?",
            "How do you feel about your \1?"
        ],
    r'.*(covid|lockdown|masks|pandemic).*':
        [
            "Although best for us, the new norm has been difficult to adjust to.",
            "Such occurrences have been natural to human history. Surely, we can overcome it.",
            "How has it affected your life?"
        ],
    r' I hate (.*)':
        [
            "When did you decide you truly hate %s?",
            "Were there incidents that made you come to this conclusion?",
            "Could you share few reasons why you hate %s?"
        ],
    r'.*(anxiety|panic|fear|tremble).*':
        [
            "How do you usually manage such situations?",
            "How long has this been part of your life?",
            "There can be ways to manage this and continue with your daily routines"
        ],
    r' (.*) makes me happy.':
        [
            "That’s wonderful. You should continue to pursue such feelings.",
            "Are there other feelings you associate with %s?",
            "How often do you make time for %s?"
        ],
    r' How can I stop (.*)?':
        [
            "Well what reasons typically can you associate with %s?",
            "What avenues have you pursued in the past?",
            "Has %s been recent or ongoing for some time?"
        ],
    r' (I am|I’m) not ready (for|to) (.*)':
        [
            "What makes you think you’re not ready for|to %s?",
            "Did you at least try to %s?",
            "What do you think can prepare you to %s?"
        ],
    r' I do\’?n?o?t have (.*)':
        [
            "Did you try earning %s?",
            "What was the last thing you did to earn %s?",
            "Do you know anyone with that %s?",
            "Do you know anyone who earned that %s and how?",
            "Perhaps there are some sources available that teaches you how to get %s"
        ],
    r' I do\'?n?o?t want (.*)':
        [
            "Have you ever had %s?",
            "What motivated you to not want %s?",
            "Do you want something else?",
            "What do you want now then? Other than %s?"
        ],
    r' (.*) divorce (.*)':
        [
            "Are you sure about pursuing this choice?",
            "What happened?",
            "Have you talked to your partner about this choice?"
        ]
}

pronoun = {
    'you': "I",
    "yours": "mine",
    "your": "my",
    "you will": "I will",
    "you have": "I have",
    "you can": "I can",
}


def transform(match):
    tokenizer = word_tokenize(match)

    for x, token in enumerate(tokenizer):
        if token in pronoun:
            tokenizer[x] = pronoun[token]
    return ' '.join(tokenizer)


def conversation_input(user_input):
    for pattern, responses in conversation_dict.items():

        ans = re.search(pattern, user_input.rstrip(",.!"))

        if ans:
            response = random.choice(responses)
            if "%s" in response:
                match = ans[1]

                pronoun = transform(match)
                response = response % (pronoun)
                return response
            else:
                return response


def answer(user_name):
    name = input('[%s] ' % user_name)
    return name


def welcome(user_name):
    print("[Eliza] Welcome %s. What would you like to share with me today?" % user_name)

    end = [r'.*bye.*', r'.*exit.*']

    while True:
        user_input = answer(user_name)
        print()
        user_input = user_input.lower()

        find_quits = 0

        for i in end:
            matches = re.findall(i, user_input)
            find_quits += len(matches)

        if find_quits == 0:
            response = conversation_input(user_input)
            print("[Eliza] " + response)
        else:
            print("[Eliza] Goodbye ")
            break


def input_name():
    name = input('[User] ')
    return name


def start_chat():
    print("[Eliza]: Hello. I'm Eliza, a psychotherapist. Who do I have the pleasure of speaking to today?")

    user_name = 'User'
    name_input = input_name()
    print()

    tokenizer = word_tokenize(name_input)

    if "name" not in name_input:
        user_name = name_input
    else:
        user_name = tokenizer[-1]
    return user_name


def main():
    user_name = start_chat()
    welcome(user_name)


if __name__ == '__main__':
    main()
