import discord
from discord.ext import commands


class Simple(discord.ui.View):
    def __init__(self, *,
                 timeout: int = 60,
                 PreviousButton: discord.ui.Button = discord.ui.Button(label="<"),
                 FirstButton: discord.ui.Button = discord.ui.Button(label="<<"),
                 LastButton: discord.ui.Button = discord.ui.Button(label=">>"),
                 NextButton: discord.ui.Button = discord.ui.Button(label="<"),
                 PageCounterStyle: discord.ButtonStyle = discord.ButtonStyle.grey,
                 InitialPage: int = 0,
                 ephemeral: bool = False) -> None:
        self.PreviousButton = PreviousButton
        self.FirstButton = FirstButton
        self.LastButton = LastButton
        self.NextButton = NextButton
        self.PageCounterStyle = PageCounterStyle
        self.InitialPage = InitialPage
        self.ephemeral = ephemeral

        self.pages = None
        self.ctx = None
        self.message = None
        self.current_page = None
        self.page_counter = None
        self.total_page_count = None

        super().__init__(timeout=timeout)

    async def start(self, ctx: discord.Interaction|commands.Context, pages: list[discord.Embed]):
        
        self.pages = pages

        self.total_page_count = len(pages)
        self.ctx = ctx
        self.current_page = self.InitialPage

        self.PreviousButton.callback = self.previous_button_callback
        self.FirstButton.callback = self.first_button_callback
        self.LastButton.callback = self.last_button_callback
        self.NextButton.callback = self.next_button_callback

        self.page_counter = SimplePaginatorPageCounter(style=self.PageCounterStyle,
                                                       TotalPages=self.total_page_count,
                                                       InitialPage=self.InitialPage)
        self.add_item(self.FirstButton)
        self.add_item(self.PreviousButton)
        self.add_item(self.page_counter)
        self.add_item(self.NextButton)
        self.add_item(self.LastButton)

        self.message = await ctx.send(embed=self.pages[self.InitialPage], view=self)

    async def first(self):
        if self.current_page != 0:
            self.current_page = 0

        self.page_counter.label = f"1/{self.total_page_count}"
        await self.message.edit(embed=self.pages[self.current_page], view=self)

    async def previous(self):

        if self.current_page == 0:
            self.current_page = self.total_page_count - 1
        else:
            self.current_page -= 1

        self.page_counter.label = f"{self.current_page + 1}/{self.total_page_count}"
        await self.message.edit(embed=self.pages[self.current_page], view=self)


    async def last(self):
        if self.current_page != self.total_page_count - 1:
            self.current_page = self.total_page_count - 1
            
        self.page_counter.label = f"{self.total_page_count}/{self.total_page_count}"
        await self.message.edit(embed=self.pages[self.current_page], view=self)

    async def next(self):

        if self.current_page == self.total_page_count - 1:
            self.current_page = 0
        else:
            self.current_page += 1

        self.page_counter.label = f"{self.current_page + 1}/{self.total_page_count}"
        await self.message.edit(embed=self.pages[self.current_page], view=self)
    
    async def first_button_callback(self, interaction: discord.Interaction):
        if interaction.user != self.ctx.author:
            embed = discord.Embed(description="**Bu butonu sen kullanamazsın çünkü sen çalıştırmadın bu komutu**.",
                                color=discord.Colour.red())
            return await interaction.response.send_message(embed=embed, ephemeral=True)
        await self.first()
        await interaction.response.defer() 

    async def last_button_callback(self, interaction: discord.Interaction):
        if interaction.user != self.ctx.author:
            embed = discord.Embed(description="**Bu butonu sen kullanamazsın çünkü sen çalıştırmadın bu komutu**.",
                                color=discord.Colour.red())
            return await interaction.response.send_message(embed=embed, ephemeral=True)
        await self.last()
        await interaction.response.defer() 
    
    async def next_button_callback(self, interaction: discord.Interaction):

        await interaction.response.defer()
        if interaction.user != self.ctx.author:
            embed = discord.Embed(description="**Bu butonu sen kullanamazsın çünkü sen çalıştırmadın bu komutu**.",
                                color=discord.Colour.red())
            return await interaction.response.send_message(embed=embed, ephemeral=True)
        await self.next()

    async def previous_button_callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        if interaction.user != self.ctx.author:
            embed = discord.Embed(description="**Bu butonu sen kullanamazsın çünkü sen çalıştırmadın bu komutu**.",
                                color=discord.Colour.red())
            return await interaction.response.send_message(embed=embed, ephemeral=True)
        await self.previous()


class SimplePaginatorPageCounter(discord.ui.Button):
    def __init__(self, style: discord.ButtonStyle, TotalPages, InitialPage):
        super().__init__(label=f"{InitialPage + 1}/{TotalPages}", style=style, disabled=True)