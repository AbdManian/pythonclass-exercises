import ui

def verify(password):
    return False, "NOK!", 0


if __name__ == '__main__':
    root = ui.get_ui_root(verify)
    root.mainloop()