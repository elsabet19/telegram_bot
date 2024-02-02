import  telegram.ext

Token ="6868604203:AAF_olh5gnYvtfYma846p8PVYH5rk796ce8"

updater = telegram.ext.Updater("6868604203:AAF_olh5gnYvtfYma846p8PVYH5rk796ce8" .use_context =True)
dispatcher = updater.dispatcher

def start(updater, use_context):
   update.message.replay_text("Hello welcome to sabahar ethiopia")

   def help(update,context):
      update.message.reply-text(
         ""
    /start -> welcome to the channel
    /help -> This Particular message
    /content -> About various Playlist of simplilearn
    /python -> The first video from python Playlist
    /Sql -> The first video from Sql Playlist
    /java ->The first video from java playlist
    /contact -> contact information 
    ""
      )

def content(update,context):
   update.message.replay_text("we have globally-minded modern design results")

  def python(update,context):
   update.message.replay_text("our uniqe products: https://sabahar.com/ ")

   def Sql(update,context):
   update.message.replay_text("our uniqe products: https://sabahar.com/")

 def java(update,context):
   update.message.replay_text("our uniqe products: https://sabahar.com/ ")

 def contact(update,context):
   update.message.replay_text("you can contact on the registered email id provided on the website")

   dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
   dispatcher.add_handler(telegram.ext.CommandHandler('start', python))
   dispatcher.add_handler(telegram.ext.CommandHandler('start', Sql))
   dispatcher.add_handler(telegram.ext.CommandHandler('start', java))
   dispatcher.add_handler(telegram.ext.CommandHandler('start', contact))
   dispatcher.add_handler(telegram.ext.CommandHandler('help', help))

   updater.start_polling()
   updater.idle(1)
   