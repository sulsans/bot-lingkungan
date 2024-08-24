import discord
from discord.ext import commands
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def jenissampah(ctx):
    await ctx.send('sampah dibagi menjadi dua jenis yaiyu organik dan nonorganik.sampah organik adalah sampah yang bisa terurai secara alami seperti sampah makanan.sampah nonorganik adalah sampah yang tidak bisa terurai secara alami seperti plastik,batre,dll')

@bot.command()
async def cara_menjaga_kebersihan(ctx):
    await ctx.send('kamu bisa menjaga kebersihan di rumah mulai dari membersihkan lantai,membersihkan barang barang,mencuci pakaian menyapu halaman,mengelola sampah,dan mendaur ulang sampah')
    
bot.run("")
