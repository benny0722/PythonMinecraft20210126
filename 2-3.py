from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random,time
while True:
    x,y,z = mc.player.getTilePos()
    
    color = random.randrange(0,2)
    mc.setBlocks(x+15,y,z+15,x-15,y,z-15,46,color)
    time.sleep(3)

