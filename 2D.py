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
    w = dx + pack[0]
    h = dy + pack[1]

    if( (w > bin.width) or (h > bin.height) ):
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
    x = pack.x + pack.width
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

def fitPack(pack, bins):
    for bin in bins:
        dx, dy = bin.width/2, bin.height/2

        if fit(pack, bin, dx, dy):
            x, y = dx + bin.x, dy + bin.y
            w, h = pack[0], pack[1]

            p = Rect(x, y, w, h)
            bins.remove(bin)
                
            for new_bin in splitBin(bin, p):
                bins.append(new_bin)
            
            print("no fitP len:", len(bins))
            bins.sort(key=lambda x: x.width)

            return  bins, p

    # No space for this package!    
    return bins, None
            
def solve(bins, packs):
    packs.sort(key=lambda x: x[0], reverse=True)

    used_packs = []
    new_bins = bins

    for pack in packs:
        print("|||||||||||||||||||||||||||||")
        for b in new_bins:
            print(b.x, b.y, b.width, b.height)
        new_bins, p = fitPack(pack, new_bins)

        if p != None:
            used_packs.append(p)

    return [used_packs, new_bins]


class Rect():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

"""
b = [ Rect(0, 0, 100, 100) ]
p = (40, 50) # dx 20 dy 30
new_bins, p = fitPack(p, b)

for b in new_bins:
    print(b.x, b.y, b.width, b.height)
"""

if __name__ == '__main__':
    w = 100
    h = 100
    scale = 7

    packs = [(i,i) for i in range(1, 100)]

    bins = [ Rect(0, 0, 100, 100) ]
    [used_packs, new_bins] = solve(bins, packs)

    master = Tk()    
    w = Canvas(master, width = scale*w, height = scale*h, bg = 'red')

    print("|||||||||||||||||||||||||||||")
    for pack in used_packs:
        print(len(used_packs))
        print(pack)
        x, y, width, height = pack.x, pack.y, pack.width, pack.height
        w.create_rectangle(scale*x, scale*y, scale*x + scale*width, scale*y + scale*height, fill="blue") 
        w.create_text(scale* (x+width/2), scale*(y+height/2),text=str(width)+"x"+str(height)) 
        print(x,y,width,height)
  
    w.pack()
    mainloop() 
