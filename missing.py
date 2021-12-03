
def writemissing(title,bm):
    if(bm=='movie'):
        with open('missingmovie.csv','a') as f:
            f.write(title)
    else:
        with open('missingbook.csv','a') as f:
            f.write(title)

