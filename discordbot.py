# インストールした discord.py を読み込む
import discord
import re 
# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NjE5MDEwOTgyMTMxMjY5NjM4.XXCDFQ.VtNeCj0Xwqr3E2Se4g_qLf2MyLk'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ありすログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if re.search(r'ありす',message.content) :
        await message.channel.send('橘です!!!')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)