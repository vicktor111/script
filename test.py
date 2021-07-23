import sys
import time
# import math
sys.path.append("C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages")
import bpy
import keyboard


print("Start.")
bpy.app.handlers.frame_change_pre.clear()
dict={
    90: 1.5707963267948966,
    180: 3.141592653589793,
    0: 0.0,
    -90: -1.5707963267948966,
    -180: -3.141592653589793
}

class Object:

    def __init__(self, speed: float = 0.5):
        self.r = 0.0
        self.speed = speed
        self.location = bpy.data.objects[bpy.context.object.name].location
        self.rotation = bpy.data.objects[bpy.context.object.name].rotation_euler

    def w(self):
        if dict[0] == self.rotation[2]:
            translate(self.location[0], self.location[1] + self.speed)
        if dict[90] == self.rotation[2]:
            translate(self.location[0] + self.speed, self.location[1])
        if dict[180] == self.rotation[2]:
            translate(self.location[0], self.location[1] - self.speed)
        if dict[-90] == self.rotation[2]:
            translate(self.location[0] - self.speed, self.location[1])

    def s(self):
        if dict[0] == self.rotation[2]:
            translate(self.location[0], self.location[1] - self.speed)
        if dict[90] == self.rotation[2]:
            translate(self.location[0] - self.speed, self.location[1])
        if dict[180] == self.rotation[2]:
            translate(self.location[0], self.location[1] + self.speed)
        if dict[-90] == self.rotation[2]:
            translate(self.location + self.speed, self.location[1])

    def a(self):
        time.sleep(0.5)
        self.r += dict[90]
        #print(self.r * 180 / math.pi)
        if self.r == 4.71238898038469:
            #print("1")
            self.rotation[2] = dict[-90]
        else:
            self.rotation[2] = self.r
        
    def d(self):
        time.sleep(0.5)
        self.r -= dict[90]
        #print(self.r * 180 / math.pi)
        if self.r == -4.71238898038469:
            #print("2")
            self.rotation[2] = dict[90]
        else:
            self.rotation[2] = self.r

mesh=Object(2.0)

def translate(x, y):
    bpy.data.objects[bpy.context.object.name].location[0] = x
    bpy.data.objects[bpy.context.object.name].location[1] = y

def path(self, value):
    if keyboard.is_pressed("w"):
        mesh.w()
    if keyboard.is_pressed("s"):
        mesh.s()
    if keyboard.is_pressed("a"):
        mesh.a()
    if keyboard.is_pressed("d"):
        mesh.d()
    if keyboard.is_pressed("ctrl"):
            bpy.app.handlers.frame_change_pre.clear()
            bpy.ops.screen.animation_step()

bpy.app.handlers.frame_change_pre.append(path)