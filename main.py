from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
import news_fetch as news
import query_formater as query 

API_KEY = '1920559871:AAEfHMl-LVwaZNnfMNTUn3551iVo9mcuwX8'

print("bot started")

def start_command(update, context):
    update.message.reply_text('Hello there! I\'m a echo bot \U000026C4 with a superpower.I fetch news headlines from all over the world. Try something like /news "category" (without double qoutes). You can add multiple queries just add space in between. Default news is tech. Have fun!')

def help_command(update, context):
    update.message.reply_text('Try something like /news technology bitcoin. You can add multiple queries just add space in between. Default news is tech. Have fun!')

def news_command(update, context):
    q = query.fun(update.message.text).lower()
    ans = news.fetch(q)
    update.message.reply_text(ans)

def handle_message(update, context):
    text = str(update.message.text)
    update.message.reply_text(text)

def error(update, context):
    print(f"update {update} caused error {context.error}")


if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('news', news_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    # Runing the bot
    updater.start_polling()
    updater.idle()