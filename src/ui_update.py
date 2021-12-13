from PySide6.QtWidgets import QSlider

from imports import *


# ############### Progressbar Thread ###########################
################################################################
class Runner(QThread):
    progress = Signal(int)
    time_changed = Signal(int)

    def __init__(self, n, c):
        super(Runner, self).__init__(parent=None)
        self.n = n
        self.c = c

    def run(self):
        for i in range(self.n):
            time.sleep(1)
            self.c -= 1
            self.progress.emit(i)
            self.time_changed.emit(self.c)


# ############## Change status Bar size on tab switch #####
###########################################################
def default_status_size(p):
    id = p.tabs.currentIndex()
    if id == 1 or id == 2 or id == 3:
        p.playActions.setMaximumHeight(0)
        p.playActions.setMinimumHeight(0)
        p.statusBar.setMaximumHeight(0)
        p.statusBar.setMinimumHeight(0)
    else:
        p.playActions.setMaximumHeight(40)
        p.playActions.setMinimumHeight(40)
        p.statusBar.setMaximumHeight(80)
        p.statusBar.setMinimumHeight(80)


# ############## Toggle status Bar ########################
###########################################################
def hide_sideBar(s):
    mini = s.sideBar.minimumWidth()
    maxi = s.sideBar.maximumWidth()
    if mini == 235 and maxi == 235:
        s.sideBar.setMinimumWidth(0)
        s.sideBar.setMaximumWidth(0)
    else:
        s.sideBar.setMinimumWidth(235)
        s.sideBar.setMaximumWidth(235)


# ################## Reset Ui settings ##############################
#####################################################################
def reset_status(s):
    s.mixer.stop()
    s.mixer.unload()
    s.progress.setValue(0)
    s.repeater.setChecked(False)
    s.tabsOff.setChecked(False)
    s.tabsOn.setChecked(False)
    s.forward.setChecked(False)
    s.backward.setChecked(False)
    s.showTabs.setChecked(False)
    s.hideTabs.setChecked(False)
    s.moveTabs.setChecked(False)
    s.moveTabsOff.setChecked(False)
    s.repeater1.setChecked(False)
    s.duration.setText("0:00:00")


# ############### Update progressbar ######################
# ############### Working partially and will be fixed latter
def load_progress(s, song):
    s.ln = s.music_length(song)
    s.r = Runner(int(s.length), s.length)
    if not s.mixer.get_busy():
        s.progress.setRange(0, s.length)
    else:
        pos = s.mixer.get_pos()
        s.progress.setValue(pos)
        s.progress.setRange(pos, s.length)
        s.r.progress.connect(s.update_progress)
        s.r.time_changed.connect(s.update_time)
        s.r.start()


def reset_progress(s):
    s.progress.setValue(0)
    s.update_current("")
    s.length = 0
