'''时间回复

简单的交互功能
是一个插件示例
'''

import OlivaBiliLive  # 命名空间

from OlivaBiliLive.plugin import BotPlugin, DanmakuMessage
from datetime import datetime

class TimeChecker(BotPlugin):  # 类名`TimeChecker`将会被作为该插件的命名空间加载，具体显示在日志中。
    async def on_command_received(self, cmd, data):  # 异步
        if cmd != 'DANMU_MSG':
            return
        danmu = DanmakuMessage.from_command(data['info'])
        if danmu.msg != '!时间':
            return
        now = datetime.now()
        show = now.strftime('%Y{y}%m{m}%d{d}').format(y='年', m='月', d='日')
        await self.send_message(f'现在的时间为: {show}')
