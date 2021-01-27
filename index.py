import discord, os, random, datetime, asyncio, datetime, token
token = os.getenv("token")
client = discord.Client()

@client.event
async def on_ready():
        await client.change_presence(
        status=discord.Status.online,
        activity=discord.Game('나는 기여운 이아리!'))
        await asyncio.sleep(2)
        cli = client.latency
        await client.change_presence(
        status=discord.Status.online,
        activity=discord.Game('접두사는 아리야!'))
        await asyncio.sleep(3)
        cli = len(client.guilds)
        await client.change_presence(
        status=discord.Status.online,
        activity=discord.Game(f'{cli}개의 서버가 저를 사용하고 있어요!'))
        await asyncio.sleep(3)
        cli = len(client.guilds)
        
      
@client.event
async def on_message(message):
  if message.content == "아리야 핑":
        embed = discord.Embed(title = ':ping_pong: 퐁!', description = str(client.latency) + 'ms', color = 0x62c1cc)
        await message.channel.send(embed=embed)
  if message.content == "이아리":
        embed=discord.Embed(title='제 이름을 부르셨나용?', description = "", color = 0x000000)      
        await message.channel.send(embed=embed)
  if message.content == '아리야 안녕':
        a = ['반가워요!', '안녕하세요!', '안녕하세여!']
        await message.channel.send(random.choice(a))
  if message.content == '아리야 주사위':
        d = ['1! 이네요', '4! 이네요', '3! 이네요', '2! 이네요', '6! 이네요', '!!! 아주 낮은 확률로 주사위가 섰습니다!!', '5! 이네요', '8! 이네요', '행운의 7! 이네요', '9! 이네요', '10! 이네요'] 
        await message.channel.send(random.choice(d))
  if message.content == "아리야 내정보":
      user = message.author
      date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
      print(date)
      await message.channel.send(f"{message.author.mention}님의 디스코드 가입일 : {date.year}/{date.month}/{date.day}")
      await message.channel.send(f"{message.author.mention}님의 이름 / 아이디 / 닉네임 : {user.name} / {user.id} / {user.display_name}")
      await message.channel.send(f"{message.author.mention}님의 프로필 : {user.avatar_url}")
  if message.content == "아리야 너정보":
        embed=discord.Embed(title='저는 2021/01/18 에 만들어졌어요 / 저의 닉네임은 이아리에요! / 저의 프로필은', description = " https://cdn.discordapp.com/attachments/787229487723970560/800543117395886120/78aa8a7658c88092.png ", color = 0x000000)      
        await message.channel.send(embed=embed)
  if message.content == "아리야 잘가":
        embed=discord.Embed(title='네? 제가 어디를 가야햐죠>?', description = "어디를 가야하오,,", color = 0x000000)      
        await message.channel.send(embed=embed)
  if message.content == "아리야 블스":
        embed=discord.Embed(title='블스님은 저의 제작자입6니다', description = "블스님 사랑해요!", color = 0x000000)      
        await message.channel.send(embed=embed)
  if message.content == "아리야 제작자":
        embed=discord.Embed(title='저의 제작자는 블스님입니다', description = "+명령어 만드는걸 도와주신분은 오리너구리님입니다", color = 0x000000)      
        await message.channel.send(embed=embed)
  if message.content == "아리야 생겨난 계기":
        embed=discord.Embed(title='블스님이 알려주셨는데 심심해서 만들었데요', description = "블스님 사랑해요!", color = 0x000000)      
        await message.channel.send(embed=embed)
  if message.content == '아리야': 
        c = ['전 졸리니 말걸지 말아여', '왜부르셨나여?',  '왜여?']
        await message.channel.send(random.choice(c))
  if message.content == "아리야 바보":
        await message.channel.send("두리번~ 두리번~ 여기에 바보있나요? 혹시 나말하는곤가,,,,?")
  if message.content == "아리야 론다":
        embed=discord.Embed(title='론다님은 제가 재일 좋아하는 스트리머 분이에여!', description = "♥", color = 0x000000)      
        await message.channel.send(embed=embed)
  if message.content == "아리야 출첵":
        embed=discord.Embed(title='출첵해주셔서 감사합니다', description = "👍👍", color = 0x000000)      
        await message.channel.send(embed=embed)
        await message.add_reaction("👍") #stun

client.run(token)    
