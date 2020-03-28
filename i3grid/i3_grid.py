import sys
import i3grid

def main():
    SIZE = 3
    ws = i3grid.new_ws(i3grid.get_ws(), sys.argv[1], SIZE)
    i3grid.set_ws(ws)
