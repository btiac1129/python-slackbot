import random

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.dispatcher import Message
import re

@listen_to("roll (\d*)d(\d+)", re.IGNORECASE)
def hello(msg: Message, number_of_die: str, side_of_die: str):
    roll_result = [random.randrange(1, int(side_of_die), 1) for i in range(int(number_of_die))]
    roll_sum = sum(roll_result)
    msg.send(str(roll_result))
    msg.send(str(roll_sum))

@respond_to("hi", re.IGNORECASE)
def hi(msg: Message):
    msg.reply("Thank you 39!")
    

