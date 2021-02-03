import random, re
from random import randint
from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

ANIMAL2 = (
  "Tiger",
  "Dear",
  "Bear",
  "Giraffe",
)

ANIMAL3 = (
  "Elephant",
  "Zebra",
  "Snake",
  "Chimpanzee",
  "Lion",
  "Otter",
)

ANIMAL4 = (
  "Tiger",
  "Zebra",
  "Dear",
  "Snake",
  "Giraffe",
  "Chimpanzee",
  "Otter",
  "Walrus",
)

HINT_ANIMAL2 = (
  "Hint for Animal game played between 2 players - 1) Tiger 2) Dear 3) Bear 4) Giraffe"
  "Hint for Animal game played between 2 players - 1) Tiger, 2) Dear, 3) Bear, 4) Giraffe"
)

HINT_ANIMAL3 = (
  "Hint for Animal game played between 3 players - 1) Elephant 2) Zebra 3) Snake 4) Chimpanzee 5) Lion 6) Otter"
  "Hint for Animal game played between 3 players - 1) Elephant, 2) Zebra, 3) Snake, 4) Chimpanzee, 5) Lion, 6) Otter"
)

HINT_ANIMAL4 = (
  "Hint for Animal game played between 4 players - 1) Tiger 2) Zebra 3) Dear 4) Snake 5) Giraffe 6) Chimpanzee 7) Otter 8) Walrus"
  "Hint for Animal game played between 4 players - 1) Tiger, 2) Zebra, 3) Dear, 4) Snake, 5) Giraffe, 6) Chimpanzee, 7) Otter, 8) Walrus"
)

@run_async
def animal2(bot: Bot, update: Update):
  update.message.reply_text(random.choice(ANIMAL2))

)

@run_async
def animal3(bot: Bot, update: Update):
  update.message.reply_text(random.choice(ANIMAL3))

)

@run_async
def animal4(bot: Bot, update: Update):
  update.message.reply_text(random.choice(ANIMAL4))

)

@run_async
def hint_animal2(bot: Bot, update: Update):
  update.message.reply_text(random.choice(HINT_ANIMAL2))
