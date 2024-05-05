from twitchio.ext import commands

counts_file = 'counts.txt'
connect_file = 'connect.txt'
emotes_file = 'emotes.txt'
emote_counts = {}
target_emotes = []
bar_window_location = (100, 100)

class TwitchBot(commands.Bot):

    def __init__(self):
        connect_settings = read_settings(connect_file)
        read_emotes(emotes_file)

        token = connect_settings.get('TOKEN')
        prefix = connect_settings.get('BOT_PREFIX')
        channel = connect_settings.get('CHANNEL')
        client_secret = connect_settings.get('CLIENT_SECRET')
        super().__init__(token=token, prefix=prefix, initial_channels=[channel], client_secret=client_secret)

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        # Ignore messages from the bot
        if message.echo:
            return

        # Print the contents of the message
        #print(message.content)

        for emote in target_emotes:
            if emote in message.content:
                count = str(message.content).count(emote)
                update_emote_count(emote, count)

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)


def read_settings(file_path):
    settings = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split each line into key and value
                key, value = line.strip().split('=')
                settings[key] = value
    except FileNotFoundError:
        print(f"Settings file not found: {file_path}")
    except Exception as e:
        print(f"Error reading settings: {e}")
    return settings


def read_emotes(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                target_emotes.append(line.strip())
        print(f"{len(target_emotes)} emotes loaded for counting.")
    except FileNotFoundError:
        print(f"Settings file not found: {file_path}")
    except Exception as e:
        print(f"Error reading settings: {e}")


# Count the emote (increment or add)
def update_emote_count(emote, count=1):
    if emote in emote_counts:
        emote_counts[emote] += count
    else:
        emote_counts[emote] = count
    print(f"Emote count updated: {emote} = {emote_counts[emote]}")

    # Order the emote counts
    # sorted_emote_counts = dict(sorted(emote_counts.items(), key=lambda item: item[1], reverse=True))

    with open(counts_file, 'w') as file:
        for key, value in emote_counts.items():
            output = f"{key},{value}\n"
            file.write(output)


if __name__ == "__main__":
    bot = TwitchBot()
    bot.run()
    input("Press enter to close the bot...")
