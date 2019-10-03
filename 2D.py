from tkinter import *

# split vertical
# split horizontal
# sort ascending
# sort descending
# sort bin ascending
# sort bin descending
# initial position (0,0)
# initial position (w/2, 0)
# initial position (0, h/2)
# initial position (w/2, h/2)

def fit(pack, bin, dx, dy):
    x = dx + pack[0]
    y = dy + pack[1]

    maxBinX = bin.x + bin.width
    maxBinY = bin.y + bin.height

    if( (x > maxBinX) or (y > maxBinY) ):
        return False
    return True

def splitBin(bin, pack):
    new_bins = []

    # Left bin
    x = bin.x
    y = bin.y

    w = pack.x - x
    h = bin.height

    new_bin = Rect(x, y, w, h)
    if(w > 0 and h > 0):
        new_bins.append(new_bin)

    # Right bin
    x = bin.x + pack.width
    y = bin.y

    w = bin.width - (pack.x + pack.width)
    h = bin.height

    new_bin = Rect(x, y, w, h)
    if(w > 0 and h > 0):
        new_bins.append(new_bin)

    # Up bin
    x = pack.x
    y = bin.y

    w = pack.width
    h = pack.y - bin.y

    new_bin = Rect(x, y, w, h)
    if(w > 0 and h > 0):
        new_bins.append(new_bin)

    # Down bin
    x = pack.x
    y = pack.y + pack.height

    w = pack.width
    h = bin.height -(pack.y + pack.height)

    new_bin = Rect(x, y, w, h)
    if(w > 0 and h > 0):
        new_bins.append(new_bin)

    return new_bins

def solve(bins, packs):
    packs.sort(key=lambda x: x[0])

    used_packs = []
    
    print("Bins len:", len(bins))
    for pack in packs:
        print("* Bins len:", len(bins))
        used = False
        for bin in bins:
            dx, dy = 0, 0

            if not used and fit(pack, bin, dx, dy):
                used = True
                x, y = dx + bin.x, dy + bin.y
                w, h = pack[0], pack[1]

                p = Rect(x, y, w, h)
                used_packs.append(p)

                bins.remove(bin)
                #packs.remove(pack)

                for new_bin in splitBin(bin, p):
                    bins.append(new_bin)
                    print(new_bin.x, new_bin.y, new_bin.width, new_bin.height)
                bins.sort(key=lambda x: x.width)
                print("**Bins len:", len(bins))
    
    print("Bins len:", len(bins))
    return [used_packs, bins]


class Rect():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

if __name__ == '__main__':
    w = 100
    h = 100
    scale = 15

    packs = [(i,i) for i in range(1, 50)]

    initial_bin = Rect(0, 0, 100, 100)
    bins = []

    bins.append(initial_bin)
    
    [used_packs, new_bins] = solve(bins, packs)

    master = Tk()    
    w = Canvas(master, width = scale*w, height = scale*h, bg = 'red')

    print("|||||||||||||||||||||||||||||")
    for block in used_packs:
        x, y, width, height = block.x, block.y, block.width, block.height
        w.create_rectangle(scale*x, scale*y, scale*x + scale*width, scale*y + scale*height, fill="blue") 
        w.create_text(scale* (x+width/2), scale*(y+height/2),text=str(width)+"x"+str(height)) 
        print(x,y,width,height)
  
    w.pack()
    mainloop()  