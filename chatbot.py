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
import time
from threading import Timer
import datetime

conversation_dict = {

    r'.*(kids?|child(ren)?).*':
        [
            "Can you tell me more about your %s?",
            "How would you describe your relationship with your %s?",
            "What do you enjoy doing with your %s?"
        ],

    r'i lost (.*)':
        [
            "I'm sorry to hear that. Can you tell me what happened?",
            "That must be tough. How are you feeling now?",
            "How are you dealing with the loss of %s?"
        ],

    r'.*(depressed|sad|pressured?|stress(ed)?).*':
        [
            "Why do you feel %s?",
            "Have you talked to anyone about how you are feeling?",
            "How do you prefer managing feeling %s?"
        ],
    r'.*(kill(ing|ed)?|suicide|die).*':
        [
            "Please stop dwelling on such thoughts. Do you share these thoughts with others in your life?",
            "Would you like to call the National Suicide Prevention Lifeline at 1-800-273-8255 (Talk)? The toll-free confidential Lifeline is available 24 hours a day, seven days a week",
            "This eliminates the possibility of improving the situation. Surely, we can find a solution"
        ],
    r'.*(job|work|career).*':
        [
            "Do you like what you do?",
            "Can you tell me more about your %s?",
            "How do you feel about your %s?"
        ],
    r'.*(covid|lockdown|masks|pandemic).*':
        [
            "Although best for us, the new norm has been difficult to adjust to.",
            "Such occurrences have been natural to human history. Surely, we can overcome it.",
            "How has it affected your life?"
        ],
    r'i hate (.*)':
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
    r'(.*) makes me happy':
        [
            "That’s wonderful. You should continue to pursue such feelings.",
            "Are there other feelings you associate with %s?",
            "How often do you make time for %s?"
        ],
    r'how can i stop (.*)':
        [
            "Well what reasons typically can you associate with %s?",
            "What avenues have you pursued in the past?",
            "Has %s been recent or ongoing for some time?"
        ],
    r'i am not ready (.*)':
        [
            "What makes you think you’re not ready %s?",
            "Did you at least try to %s?",
            "What do you think you can do to prepare %s?"
        ],
    r'i don\'?t? have (.*)':
        [
            "Did you try earning %s?",
            "What was the last thing you did to earn %s?",
            "Do you know anyone with %s?",
            "Do you know anyone who earned that %s and how?",
            "Perhaps there are some sources available that teaches you how to get %s"
        ],
    r'i don\'?t? want(.*)':
        [
            "Have you ever had %s?",
            "What motivated you to not want %s?",
            "Do you want something else?",
            "What do you want now then? Other than %s?"
        ],
    r'(.*) divorce (.*)':
        [
            "Are you sure about pursuing this choice?",
            "What happened?",
            "Have you talked to your partner about this choice?"
        ],
    r'(.*)':
        [
            "Can you tell me more about it?",
            "Would you mind sharing more about it?",
            "Please tell me more.",
            "How does that make you feel?"
        ],

}

pronoun = {
    "you": "me",
    "yours": "mine",
    "your": "my",
    "you will": "I will",
    "you have": "I have",
    "you can": "I can",
    "me": "you",
    "mine": "yours",
    "my": "your",
    "I will": "you will",
    "I have": "you have",
    "I can": "you can"

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
    timeout = 30
    time = Timer(timeout, print,
                 ['\n[Eliza] Hi %s. Are you still there? Is there anything more you want to tell me?\n' % user_name])
    time.start()
    name = input('[%s] ' % user_name)
    time.cancel()
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


def greet():
    currentTime = datetime.datetime.now()
    if currentTime.hour < 12:
        return "Good morning."
    elif 12 <= currentTime.hour < 18:
        return "Good afternoon."
    else:
        return "Good evening."

def start_chat():
    print("[Eliza]: %s I'm Eliza, a psychotherapist. Who do I have the pleasure of speaking to today?"%greet())
    user_name = 'User'
    name_input = input('[User] ')
    print()

    tokenizer = word_tokenize(name_input)
    user_name = tokenizer[-1]
    return user_name


def main():
    user_name = start_chat()
    welcome(user_name)


if __name__ == '__main__':
    main()
