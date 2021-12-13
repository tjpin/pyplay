from imports import *
from pyplay import Ui_MainWindow

# base_path = Path(__file__).resolve().parent
# ui, _ = loadUiType(os.path.join(base_path, "ui/pyplay.ui"))
pygame.init()


class PyPlayer(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(PyPlayer, self).__init__(parent=None)
        self.setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint))
        self.setupUi(self)
        self.setMinimumSize(900, 600)
        # ###### Initialize mixer ##############
        self.mixer = pygame.mixer.music
        self.mixer.set_volume(0.3)

        # ######### MUSIC LISTS ################
        self.playlist = PlayLists()
        self.musicList = []
        self.docList = []

        self.folder1 = ""
        self.folder2 = ""

        self.length = 0
        self.loop = 0
        self.volume = 0

        self.playing = False
        self.running_text = ""

        # ######## called on app start ###############
        self.button_callbacks()
        self.call_on_start()

    # This functions are called when app ist started.
    def call_on_start(self):
        self.check_file(self.folder1)
        self.update_from_music(self.folder2)
        self.progress.setValue(self.length)
        self.tabs.setCurrentIndex(0)
        self.add_widgets()
        self.hide_status_bar()

    def button_callbacks(self):
        self.closeBtn.clicked.connect(lambda: self.close())
        self.miniBtn.clicked.connect(lambda: self.showMinimized())

        self.volumeSlider.valueChanged.connect(lambda value: self.volume_(value))
        self.openFile.clicked.connect(lambda: hide_sideBar(self))
        self.next.clicked.connect(self.next_)
        self.prev.clicked.connect(self.previous)
        self.playPause.clicked.connect(self.play_pause)
        self.playPause_2.clicked.connect(self.play_pause)
        self.playPause_3.clicked.connect(self.play_pause)
        self.miniMaxi.clicked.connect(self.mini_maxi_window)
        self.resetBtn.clicked.connect(lambda: reset_status(self))

        ############################################################
        self.playlist.textdata.connect(self.get_data)

        # ####### Update Events #####################################
        self.titleBar.mouseMoveEvent = self.moveWindow
        self.titleBar.mouseDoubleClickEvent = self.double_max

        # ######## Radio Buttons Callbacks ###########################
        self.repeater.clicked.connect(lambda x: self.repeat())
        self.tabsOff.clicked.connect(lambda: disable_tabs(self.tabs))
        self.tabsOn.clicked.connect(lambda: enable_tabs(self.tabs))
        self.forward.clicked.connect(lambda: fast_forward(self.mixer))
        self.backward.clicked.connect(lambda: backward(self.mixer))
        self.showTabs.clicked.connect(lambda: show_tabs(self.tabs))
        self.hideTabs.clicked.connect(lambda: hide_tabs(self.tabs))
        self.moveTabs.clicked.connect(lambda: move_tabs(self.tabs))
        self.moveTabsOff.clicked.connect(lambda: disable_tab_move(self.tabs))
        self.repeater1.clicked.connect(self.repeat)

    @Slot(str)
    def get_data(self, d):
        self.running3.setText(ntpath.basename(d))

    def add_widgets(self):
        self.playBox.addWidget(self.playlist)

    # ############# Widget Events #######################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def double_max(self, event):
        if event.MouseButtonDblClick:
            if self.isMaximized():
                self.showNormal()
            else:
                self.showMaximized()

    def moveWindow(self, event):
        gpos = event.globalPosition().toPoint()
        if self.isMaximized():
            self.showNormal()
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + gpos - self.dragPos)
            self.dragPos = gpos
            event.accept()

    # ############# Load all Mp3 file ######################################
    def check_file(self, path):
        for dr, fl, files in os.walk(path):
            for index, file in enumerate(files):
                if file.endswith(".mp3"):
                    self.musicList.append(os.path.join(dr, file))
                    music = PlayButton(file)
                    music.clicked.connect(
                        lambda *args, btn=music: self.play(os.path.join(dr, btn.text)))
                    self.addMusic.addWidget(music)
                else:
                    pass

    def update_from_music(self, path):
        for dr, fl, files in os.walk(path):
            for index, file in enumerate(files):
                if file.endswith(".mp3"):
                    music = QListWidgetItem(file)
                    music.setIcon(QIcon("assets/play.svg"))
                    self.musicLibrary.addItem(music)
            self.musicLibrary.currentTextChanged.connect(lambda *args: self.play_music(args[0], dr))

    # ############### Play from Music directory ##############################
    def play_music(self, c, d):
        song = os.path.join(d, c)
        if self.mixer.get_busy():
            self.mixer.stop()
        try:
            self.mixer.set_volume(0.3)
            self.mixer.load(song)
            self.mixer.play(loops=self.loop)
            self.playPause_2.setIcon(QIcon("assets/pause.svg"))
            self.running_2.setText(c)
        except pygame.error:
            # Here there is a known error, will be fixed soon"
            pass

    # ############### Play Music ##############################################
    def play(self, song):
        # if self.mixer.get_busy():
        self.mixer.unload()
        reset_progress(self)
        self.mixer.load(song)
        self.mixer.play(loops=self.loop)
        self.playPause.setIcon(QIcon("assets/pause.svg"))
        self.update_current(song)
        load_progress(self, song)

    def play_pause(self):
        if self.mixer.get_busy():
            self.mixer.pause()
            self.playPause.setIcon(QIcon("assets/play.svg"))
            self.playPause_2.setIcon(QIcon("assets/play.svg"))
            self.playPause_3.setIcon(QIcon("assets/play.svg"))
        else:
            self.mixer.unpause()
            self.playPause.setIcon(QIcon("assets/pause.svg"))
            self.playPause_2.setIcon(QIcon("assets/pause.svg"))
            self.playPause_3.setIcon(QIcon("assets/pause.svg"))

    # ############## Play Next and Previous in the list #################
    def next_(self):
        self.duration.setText("0:00:00")
        play_next(self.play, self.running_text, self.musicList)
        load_progress(self, self.running_text)
        self.update_current(self.running_text)

    def previous(self):
        self.duration.setText("0:00:00")
        play_previous(self.play, self.running_text, self.musicList)
        load_progress(self, self.running_text)
        self.update_current(self.running_text)

    # ############ Change and update volume and volume slider ############################
    def volume_(self, v):
        self.volume = v / 100
        self.mixer.set_volume(self.volume)
        self.volumeDisplay.setText(f"{v}%")

    # ############ Show current song ######################################################
    def update_current(self, text):
        self.running_text = text
        self.running.setText(ntpath.basename(text))

    def repeat(self):
        if self.repeater.isChecked() or self.repeater1.isChecked():
            self.loop = -1
        elif self.repeaterOff.isChecked():
            self.loop = 0
        else:
            self.loop = 0

    # ############ Get Music Length #######################################
    def music_length(self, file):
        audio = MP3(file)
        length = audio.info.length
        length_ = time.strftime('%H:%M:%S', time.gmtime(length))
        self.length = length
        return length_

    def update_progress(self, value):
        self.progress.setValue(value)

    def update_time(self, t):
        self.duration.setText(time.strftime('%H:%M:%S', time.gmtime(t)))

    def mini_maxi_window(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def hide_status_bar(self):
        self.tabs.currentChanged.connect(lambda: default_status_size(self))


