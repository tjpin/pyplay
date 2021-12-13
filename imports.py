# ################### Optimizing imports for all files #########################
# ################### All imports are fetched from here ########################
################################################################################

from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QAbstractListModel, QUrl, Signal, QThread, QObject, Slot
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import QApplication, QMainWindow,\
    QVBoxLayout, QListView, QWidget, QFileDialog
from PySide6.QtWidgets import QListWidgetItem

from mutagen.mp3 import MP3
from pygame import mixer
import ntpath
import pygame
import time
import os
import sys
from pathlib import Path

from src.playlist import PlayLists
from widgets.play_button import PlayButton
from src.widget_callback import *
from src.audio_callback import play_next, play_previous
from src.ui_update import Runner, default_status_size, hide_sideBar, reset_status, load_progress, reset_progress

