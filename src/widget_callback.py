def disable_tabs(widget):
    widget.setDisabled(True)
    print("Disabled")


def enable_tabs(widget):
    widget.setEnabled(True)
    print("Enabled")


def move_tabs(widget):
    widget.setMovable(True)


def disable_tab_move(widget):
    widget.setMovable(False)


def show_tabs(widget):
    widget.show()


def hide_tabs(widget):
    widget.hide()


def fast_forward(mixer):
    pos = mixer.get_pos() / 1000
    pos += 100
    mixer.set_pos(pos)


def backward(mixer):
    pos = mixer.get_pos() / 1000
    pos -= 100
    if pos <= 100:
        return
    mixer.set_pos(pos)
