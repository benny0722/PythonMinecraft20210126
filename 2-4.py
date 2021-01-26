
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()

length = 10
width = 8
high = 7

block = 7
air = 0

mc.setBlocks(x,y,z,x+length,y+high,z+width,block)
mc.setBlocks(x+1,y+1,z+1,x+length-1,y+high-1,z+width-1,air)