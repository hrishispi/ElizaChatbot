# ElizaChatbot

##Header 


Eliza will begin with a greeting. The greeting itself has multiple features, including a bonus functionality. Eliza will introduce herself, recognize the time zone of the user and customize the greeting based on the local time of the user and then request the name of the user. Once a name has been entered, preferably a one word name, Eliza will welcome the user and begin her session. 

Eliza has a dictionary of pronouns and can respond logically providing back an appropriate pronoun response. So if the user mentions " my children", Eliza will request more information about "your children". 

#Add spotting examples

While there are particular keywords for which Eliza has a set of solutions, if she's unable to recognize the user's issue, Eliza will request more information in order to match the set of keywords to provide an accurate session.

To end the session, 'exit' or 'bye' will terminate the session.

```
    currentTime = datetime.datetime.now()
    if currentTime.hour < 12:
        return "Good morning."
    elif 12 <= currentTime.hour < 18:
        return "Good afternoon."
    else:
        return "Good evening."
```

- bullet 1
- bullet 2
