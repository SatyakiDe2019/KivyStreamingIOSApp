##############################################
#### Updated By: SATYAKI DE               ####
#### Updated On: 12-Nov-2021              ####
####                                      ####
#### Objective: Consuming Streaming data  ####
#### from Ably channels & captured IoT    ####
#### events from the simulator & publish  ####
#### them in Kivy-I/OS App through        ####
#### measured KPIs.                       ####
####                                      ####
##############################################

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.core.window import Window
from kivymd.app import MDApp
import datetime as dt
import datetime

from kivy.properties import StringProperty

from kivy.vector import Vector

import regex as re

import os
os.environ["KIVY_IMAGE"]="pil"

import platform as pl

import matplotlib.pyplot as plt
import pandas as p

from matplotlib.patches import Rectangle

from matplotlib import use as mpl_use
mpl_use('module://kivy.garden.matplotlib.backend_kivy')

plt.style.use('fivethirtyeight')

# Consuming data from Ably Queue
from ably import AblyRest

# Main Class to consume streaming
import clsStreamConsume as ca

# Create the instance of the Covid API Class
x1 = ca.clsStreamConsume()

var1 = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
print('*' *60)
DInd = 'Y'

Window.size = (310, 460)

Curr_Path = os.path.dirname(os.path.realpath(__file__))

os_det = pl.system()
if os_det == "Windows":
    sep = '\\'
else:
    sep = '/'

def getRealTimeIoT():
    try:
        # Let's pass this to our map section
        df = x1.conStream(var1, DInd)

        print('Data:')
        print(str(df))

        return df
    except Exception as e:
        x = str(e)
        print(x)

        df = p.DataFrame()

        return df

class MainInterface(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = getRealTimeIoT()
        self.likes = 0
        self.dcMotor = 0
        self.servoMotor = 0
        self.minRatio = 0
        plt.subplots_adjust(bottom=0.19)

        #self.fig, self.ax = plt.subplots(1,1, figsize=(6.5,10))
        self.fig, self.ax = plt.subplots()
        self.mpl_canvas = self.fig.canvas


    def on_data(self, *args):
        self.ax.clear()
        self.data = getRealTimeIoT()

        self.ids.lk_img_1.source = Curr_Path + sep + 'Background' + sep + "Likes_Btn.png"
        self.likes = self.getMaxLike(self.data)
        self.ids.dynVal.text = str(self.likes)
        self.ids.lk_img_1.source = ''
        self.ids.lk_img_1.source = Curr_Path + sep + 'Background' + sep + "Likes_Btn_R.png"

        self.dcMotor = self.getMaxDCMotor(self.data)
        self.ids.dynDC.text = str(self.dcMotor)

        self.servoMotor = self.getMaxServoMotor(self.data)
        self.ids.dynServo.text = str(self.servoMotor)

        self.minRatio = self.getDc2ServoMinRatio(self.data)
        self.ids.dynMin.text = str(self.minRatio)

        x = self.data['x_value']
        y1 = self.data['total_1']
        y2 = self.data['total_2']

        self.ax.plot(x, y1, label='Channel 1', linewidth=5.0)
        self.ax.plot(x, y2, label='Channel 2', linewidth=5.0)

        self.mpl_canvas.draw_idle()

        box = self.ids.box
        box.clear_widgets()
        box.add_widget(self.mpl_canvas)

        return self.data

    def getMaxLike(self, df):

        payload = df['x_value']
        a1 = str(payload.agg(['max']))
        max_val = int(re.search(r'\d+', a1)[0])

        return max_val

    def getMaxDCMotor(self, df):

        payload = df['total_1']
        a1 = str(payload.agg(['max']))
        max_val = int(re.search(r'\d+', a1)[0])

        return max_val

    def getMaxServoMotor(self, df):

        payload = df['total_2']
        a1 = str(payload.agg(['max']))
        max_val = int(re.search(r'\d+', a1)[0])

        return max_val

    def getMinDCMotor(self, df):

        payload = df['total_1']
        a1 = str(payload.agg(['min']))
        min_val = int(re.search(r'\d+', a1)[0])

        return min_val

    def getMinServoMotor(self, df):

        payload = df['total_2']
        a1 = str(payload.agg(['min']))
        min_val = int(re.search(r'\d+', a1)[0])

        return min_val

    def getDc2ServoMinRatio(self, df):

        minDC = self.getMinDCMotor(df)
        minServo = self.getMinServoMotor(df)
        min_ratio = round(float(minDC/minServo), 5)

        return min_ratio

    def update(self, *args):
        self.data = self.on_data(self.data)

    def pressed(self, instance, inText, SM):

        if str(inText).upper() == 'START':
            instance.parent.ids.s_img.source = Curr_Path + sep + 'Background' + sep + "Pressed_Start_Btn.png"
            print('In Pressed: ', str(instance.parent.ids.s_img.text).upper())
            if ((SM.current == "background_2") or (SM.current == "background_3")):
                SM.transition.direction = "right"
            SM.current= "background_1"
            Clock.unschedule(self.update)
            self.remove_widget(self.mpl_canvas)

        elif str(inText).upper() == 'STATS':

            instance.parent.ids.st_img.source = Curr_Path + sep + 'Background' + sep + "Pressed_Stats_Btn.png"
            print('In Pressed: ', str(instance.parent.ids.st_img.text).upper())
            if (SM.current == "background_1"):
                SM.transition.direction = "left"
            elif (SM.current == "background_3"):
                SM.transition.direction = "right"
            SM.current= "background_2"
            Clock.schedule_interval(self.update, 0.1)
        else:
            instance.parent.ids.lk_img.source = Curr_Path + sep + 'Background' + sep + "Pressed_Likes_Btn.png"
            print('In Pressed: ', str(instance.parent.ids.lk_img.text).upper())
            if ((SM.current == "background_1") or (SM.current == "background_2")):
                SM.transition.direction = "left"
            SM.current= "background_3"

            Clock.schedule_interval(self.update, 0.1)
            instance.parent.ids.dynVal.text = str(self.likes)
            instance.parent.ids.dynDC.text = str(self.dcMotor)
            instance.parent.ids.dynServo.text = str(self.servoMotor)
            instance.parent.ids.dynMin.text = str(self.minRatio)

            self.remove_widget(self.mpl_canvas)


    def released(self, instance, inrText):

        if str(inrText).upper() == 'START':
            instance.parent.ids.s_img.source = Curr_Path + sep + 'Background' + sep + "Start_Btn.png"
            print('Released: ', str(instance.parent.ids.s_img.text).upper())
        elif str(inrText).upper() == 'STATS':
            instance.parent.ids.st_img.source = Curr_Path + sep + 'Background' + sep + "Stats_Btn.png"
            print('Released: ', str(instance.parent.ids.st_img.text).upper())
        else:
            instance.parent.ids.lk_img.source = Curr_Path + sep + 'Background' + sep + "Likes_Btn.png"
            print('Released: ', str(instance.parent.ids.lk_img.text).upper())


class CustomApp(MDApp):
    def build(self):
        return MainInterface()

if __name__ == "__main__":
    custApp = CustomApp()
    custApp.run()
