# ElizaChatbot

## Description of the problem to be solved

The objective of the assignment is to design a chatbot named Eliza using Python. Eliza plays the role as a psychotherapist to carry out a dialogue with users. The program is thoughtfully designed to ensure that responses provided by Eliza are appropriate and meaningful. The program utilizes word spotting to recognize key words inputted by users, look up the key words in the dictionary, identify and convert pronouns when needed, and then lastly provide a logically pre-written response. For example, when a user inputs a statement with key word “I lost” my mom, Eliza responds with “How are you dealing with the lost of your mom?”. In the event that no key word is identified, Eliza can provide a general response to keep the conversation going.  The program should be robust enough that users would think they are speaking with a real person and not a chatbot. 

## An actual example of program input and output, along with usage instructions, including bonus functionality 

Eliza will begin with a greeting. The greeting itself has multiple features, including a bonus functionality. Eliza will introduce herself, recognize the time zone of the user and customize the greeting based on the local time of the user and then request the name of the user. Once a name has been entered, preferably a one word name, Eliza will welcome the user and begin her session. 

Eliza has a dictionary of pronouns and can respond logically providing back an appropriate pronoun response. So if the user mentions " my children", Eliza will request more information about "your children". 

## Add spotting examples

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
![Flow diagram](https://github.com/hrishispi/ElizaChatbot/blob/main/ElizaFlowDiagram.jpg?raw=true)