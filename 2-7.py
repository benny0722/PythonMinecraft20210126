from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

try:
    blocktype = int(input("請輸入要放的方塊ID:"))
    mc.setBlock(x,y,z,blocktype)
except:
    print("只能輸入數字!!!!!!")

