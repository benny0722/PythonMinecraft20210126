from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random,time
while True:
    x,y,z = mc.player.getTilePos()
    
    color = random.randrange(0,9)
    mc.setBlocks(x+1,y,z+1,x-1,y,z-1,38,color)
    time.sleep(1)

