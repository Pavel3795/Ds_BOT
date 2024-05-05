import sqlite3
from discord import Intents
from discord.ext import commands
conn = sqlite3.connect('database.db')

conn.execute('''CREATE TABLE IF NOT EXISTS PassMan(
                            passwordid INTEGER PRIMARY KEY,
                            platform TEXT NOT NULL,
                            pasword TEXT NOT NULL,
			                user_id INTEGER
                        )''')

conn.commit()
conn.close()

bot = commands.Bot(command_prefix="!", intents=Intents.all())

def infoput(platform, pasword, user_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO PassMan (platform, pasword, user_id) VALUES (?, ?, ?)', (platform, pasword, user_id))
    conn.commit()
    conn.close()

def infout(user_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM PassMan WHERE user_id = ?', (user_id,))
    user_info = cursor.fetchall()
    conn.close()
    return user_info


@bot.command()
async def addpass(ctx, platform, pasword):
    infoput( platform, pasword, ctx.author.id)
    await ctx.send(f'added')

@bot.command()
async def takeout(ctx):
    info = infout(ctx.author.id)
    await ctx.author.send(f'{info}')

    

bot.run('')