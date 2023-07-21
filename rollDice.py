'''掷骰模拟插件的示例

实现:【.r(opt=d)】
'''
import random
import re

import OlivaBiliLive

from OlivaBiliLive.plugin import BotPlugin, DanmakuMessage

def logging_info(msg:str,level=2):
    OlivaBiliLive.main.GlobalProc.log(level,f"[OlivaBiliLive] : {msg}")
    
def roll_dice(num=1,RangeNum=100) -> 'list|int':    # type: ignore
    '''返回掷骰结果
    
    '''
    DiceList = [y for x in range(1,num+1) for y in range(1,RangeNum+1)] # 存储num个骰子的1~6数字
    IndexList = [random.randint(0,len(DiceList)-1) for _ in range(num)]
    ValList = [DiceList[i] for i in IndexList]
    return ValList,sum(ValList)  # type: ignore


class Dice(BotPlugin):
    async def on_command_received(self, cmd, data):
        if cmd != 'DANMU_MSG': # 排除了不是弹幕的可能性
            return
        danmu = DanmakuMessage.from_command(data['info'])
        if danmu.msg != '.r':
            return
        numList = re.findall(r'.r(\d+)?d?(\d+)?',danmu.msg)
        try:
            RangeNum = int(numList[0][1])
        except ValueError:
            RangeNum = 100
        try:
            RollNum = int(numList[0][0])
        except ValueError:
            RollNum = 1
        DiceList,Total = roll_dice(RollNum,RangeNum) # type: ignore
        await self.send_message(f'掷骰结果: {DiceList} = {Total}')
