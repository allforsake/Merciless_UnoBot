#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from config import TOKEN, WORKERS
import logging
import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from game_manager import GameManager
from database import db

db.bind('sqlite', os.getenv('UNO_DB', 'uno.sqlite3'), create_db=True)
db.generate_mapping(create_tables=True)

gm = GameManager()

from telegram.ext import Application

if not TOKEN:
    raise ValueError("TOKEN is missing! Check config.json or environment variables.")

print(f"Using TOKEN: {TOKEN[:5]}...")

application = Application.builder().token(TOKEN).build()

def show_settings(update, context):
    chat = update.message.chat

    if update.message.chat.type != 'private':
        send_async(context.bot, chat.id, text=_("Please edit your settings in a private chat with the bot."))
        return

    us = UserSetting.get(id=update.message.from_user.id)

    if not us:
        us = UserSetting(id=update.message.from_user.id)

    if not us.stats:
        stats = '📊' + ' ' + _("Enable statistics")
    else:
        stats = '❌' + ' ' + _("Delete all statistics")

    kb = [[stats], ['🌍' + ' ' + _("Language")]]
    send_async(context.bot, chat.id, text='🔧' + ' ' + _("Settings"), reply_markup=ReplyKeyboardMarkup(keyboard=kb, one_time_keyboard=True))

def kb_select(update, context):
    chat = update.message.chat
    user = update.message.from_user
    option = context.match[1]

    if option == '📊':
        us = UserSetting.get(id=user.id)
        us.stats = True
        send_async(context.bot, chat.id, text=_("Enabled statistics!"))

    elif option == '🌍':
        kb = [[locale + ' - ' + descr] for locale, descr in sorted(available_locales.items())]
        send_async(context.bot, chat.id, text=_("Select locale"), reply_markup=ReplyKeyboardMarkup(keyboard=kb, one_time_keyboard=True))

    elif option == '❌':
        us = UserSetting.get(id=user.id)
        us.stats = False
        us.first_places = 0
        us.games_played = 0
        us.cards_played = 0
        send_async(context.bot, chat.id, text=_("Deleted and disabled statistics!"))

def locale_select(update, context):
    chat = update.message.chat
    user = update.message.from_user
    option = context.match[1]

    if option in available_locales:
        us = UserSetting.get(id=user.id)
        us.lang = option
        _.push(option)
        send_async(context.bot, chat.id, text=_("Set locale!"))
        _.pop()

# Додаємо обробники
application.add_handler(CommandHandler('settings', show_settings))
application.add_handler(MessageHandler(filters.Regex('^([' + '📊' + '🌍' + '❌' + ']) .+$'), kb_select))
application.add_handler(MessageHandler(filters.Regex(r'^(\w\w_\w\w) - .*'), locale_select))

# Запускаємо бота
application.run_polling()

