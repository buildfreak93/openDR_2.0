"""

"""
########## Modules for gui_api.py #######################
import pygame
import time
import random
import os
import urllib2
import serial
from multiprocessing import Process, Queue, Event
from PIL import Image
from datetime import datetime
import datetime
import vkeyboard
from pygame.locals import *
from vkeyboard import *
import subprocess
import argparse

########### Modules for cam_api.py ########################
from picamera import PiCamera
from threading import Thread
import cv2
import numpy as np
import io

os.system("sudo iwlist wlan0 scan | grep ESSID > network.txt")
