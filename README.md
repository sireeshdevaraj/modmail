# INSTALLING [DISCORD.PY](https://github.com/Rapptz/discord.py)
- Need Python 3.8 or higher
- Install the latest discord.py version with
```py
# Linux/macOS
python3 -m pip install -U discord.py

# Windows
py -3 -m pip install -U discord.py
```
- After installing the Dependencies all you need to do is enter the details of your Bot Token in **config.json** in the TOKEN field
- If you don't know how to get one or never created a bot before just follow the [docs here](https://discordpy.readthedocs.io/en/stable/discord.html)
# WHERE DO I CONFIGURE CHANNEL AND SERVER?
- Lock the `/report` to specific roles , configure the roles from in this [line](https://github.com/sireeshdevaraj/modmail/blob/main/main.py#:~:text=%40app_commands.checks.has_any_role(999999999999999999%2C%20999999999999999999%2C%20999999999999999999))
- Configure the **GUILD ID** in this [line1](https://github.com/sireeshdevaraj/modmail/blob/main/main.py#:~:text=main_guild%20%3D%20bot.get_guild(999999999999999999)%23Enter%20the%20Guild%20ID%20of%20the%20main%20server) and [line2](https://github.com/sireeshdevaraj/modmail/blob/main/main.py#:~:text=if%20interaction.guild.id%3D%3D681336886891118688%3A%20%23enter%20the%20Guild%20ID%20of%20the%20main%20server)
- Configure the **CHANNEL ID** in this [line](https://github.com/sireeshdevaraj/modmail/blob/main/main.py#:~:text=channel%20%3D%20bot.get_channel(999999999999999999)%23Enter%20the%20channel%20ID%20you%20want%20to%20Send%20the%20DM%20messages)
# FEATURES:
- Delivers all the messages to MOD channel
- Supports Slash commands
- Single report command to dm the user,it supports adding the image too

# I CAN'T SEE THE SLASH COMMANDS?
- That's because you didn't add the `applications.commands` in the bot scope
- Kick the bot and re-add the Scope and invite the bot with the new URL
- ![]()

# NOTE:
- This Bot is a Basic and more than enough for a server to moderate with MODMAILS 
- You can just fork this bot and add the Rich-features as you like
- Pull Requests are always welcome
