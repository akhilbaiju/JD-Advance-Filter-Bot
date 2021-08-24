from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '👉🏻 Click to Join Channel 👈🏻', url="https://t.me/honeybeemovies"
                                )
                        ]
                    ]
                )
             )
      #      await bot.send_message(
       #         chat_id=update.chat.id,
        #        text=f"<b><i>Exrtra Message needed for subscribers can be added here \n.</b> </i>",
         #       parse_mode="html",
          #      reply_to_message_id=update.message_id
           # )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '👉🏻 Click to Join Channel 👈🏻', url="https://t.me/honeybeemovies"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '👉🏻 Click to Join Channel 👈🏻', url="https://t.me/honeybeemovies"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('Youtube', url='https://www.youtube.com/channel/UCe5RaLkqRimYwdWss4FpH2w'),
        InlineKeyboardButton('Telegram', url ='https://t.me/honeybeemovies')
    ],[
        InlineKeyboardButton('⚡ Movie Updates ⚡🛠', url='https://t.me/malluflix')
    ],[
        InlineKeyboardButton('⚙ Help ⚙', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    send_messager=await bot.send_photo(
                chat_id = update.chat.id,
                photo="https://telegra.ph/file/156cfe447430f759c5d4d.jpg",
                caption=Translation.START_TEXT.format(
                update.from_user.first_name),
                reply_markup=reply_markup,
                parse_mode="html",
                reply_to_message_id=update.message_id
            )

@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
