from i3ipc import Connection

def get_ws():
    i3 = Connection()
    ws = i3.get_tree().find_focused().workspace().name
    return int(ws[0])

def new_ws(ws, direction, size):
    SIZE = size
    actions = {'u' : -SIZE, 'd' : SIZE,
               'l' : -1, 'r' : 1}
    return ws + actions[direction]

def set_ws(ws):
    i3 = Connection()
    i3.command(f'workspace number {ws}')
