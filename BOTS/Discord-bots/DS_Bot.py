
from IDkeyCOINbruh import ID_coin as token
import discord
from discord.ext import commands
import os
#import sys
#sys.path.append('../../Functions/Parser_base.py')
#from . import get_info_html

def main():
    TOKEN = token.token_ds()

    my_intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="-", intents=my_intents)


    @bot.event
    async def on_ready():
        print(f'{bot.user.name} спустился в doungeon и готов заплатить 300$ за fisting ass!')


    @bot.event
    async def on_message(message):
      if message.author.bot:
        return
      await bot.process_commands(message)


    @bot.event
    async def on_member_join(member):
        await member.send(f"Добро пожаловать в наш doungeon, {member.guild.name}.\nТеперь ты Fucken Slave\nПиши -pls_help для списка команд бота")
        role = discord.utils.get(member.guild.roles, id=989471602867585044)
        await member.add_roles(role)


    @bot.command()
    async def add_content(ctx, file_name, *, string):
        file = open(file=file_name+'.txt', mode='a+')
        file.write(f"{string}\n\n")
        file.close()
        print(f'{ctx.message.author} изменил файл {file_name}\nизменение:\n{string}')
        await ctx.send(f'Вы создали новый файл с названием {file_name} и слудуюшим содержанием:\n{string}')


    @bot.command()
    async def get_content(ctx, file_name):
        try:
            await ctx.send(file=discord.File(file_name+'.txt'))
        except FileNotFoundError:
            await ctx.send('Файла с таким именем не существует.')


    @bot.command()
    async def del_content(ctx, file_name):
        place = os.path.abspath(file_name+'.txt')
        os.remove(place)
        print(f'{ctx.message.author} удалил файл {file_name}.')
        await ctx.send(f"Вы удалили файл {file_name}")

    @bot.command()
    async def ls_content(ctx):
        os.system("chcp 1251")
        text = os.popen("dir /B").read()
        await ctx.send(text)

    @bot.command()
    async def pls_help(ctx):
        lst_commands = ["-ls_content -- просмотр всех файлов",
                        "-del_content 'имя файла' -- удаление файла",
                        "-get_content 'имя файла' -- просмотр содержания файла",
                        "-add_content 'имя файла'<тут пробел>'текст для записи в файл'"]
        await ctx.send('\n'.join(lst_commands))

    @bot.command()
    async def orders(ctx):
        os.system("chcp 1251")
        text = os.popen("dir /B").read()[10:-1:]
        text_f = text.split('\n')
        for i in range(len(text_f)):
            orders = discord.File(text_f[i])
            await ctx.send(file=orders)

    bot.run(token=TOKEN)

if __name__ == '__main__':
    main()
