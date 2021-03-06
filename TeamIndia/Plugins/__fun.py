from TeamIndia.functions.fun import *



__help__ = "Click on below buttons and check amazing tools for Fun."  

# no help string

__button__ = [ InlineKeyboardButton(text="Memes", callback_data="indiafun_"),
            InlineKeyboardButton(text="Emojis", callback_data="indiafunemoji_"),
            InlineKeyboardButton(text="Games", callback_data="indiafungames_"),

] 
__buttons__ = [InlineKeyboardButton(text="Couple", callback_data="indiafuncouple_"), 
              InlineKeyboardButton(text="Karma", callback_data="indiafunkarma_"),
]


__mod_name__ = "Fun"


dispatcher.add_handler(fun_callback_handler)
dispatcher.add_handler(fun_emoji_callback_handler)
dispatcher.add_handler(fun_games_callback_handler)
dispatcher.add_handler(fun_couple_callback_handler)
dispatcher.add_handler(fun_karma_callback_handler)
