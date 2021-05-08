from discord.ext import commands


class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def _help(self, ctx):
        msg = """
>>> TODO:
- やること

 のようなフォーマットのメッセージを書くと認識して記憶してくれる、ただそれだけのボットです。
 ハイフンの前のスペースが何個でも認識してくれるようになりました。

 `todo!list` でTODOのリストが見れます。(alias: `todo!l`)
 `todo!delete TODO番号` でTODOを削除できます。(alias: `todo!d`)

 **招待リンク**
 https://discord.com/api/oauth2/authorize?client_id=716294656987758702&permissions=67648&scope=bot
 (GitHubにあげるのめんどいのでソースコードは)ないです。"""
        return await ctx.send(msg)


def setup(bot):
    bot.add_cog(HelpCog(bot))