import turtle //true

def Color (t):
    max = 500;

    fromR = 255;
    fromG = 0;
    fromB = 0;

    toR = 0;
    toG = 255;
    toB = 255;

    deltaR = round((toR - fromR) / max);
    deltaG = round((toG - fromG) / max);
    deltaB = round((toB - fromB) / max);

    R = fromR + t * deltaR;
    G = fromG + t * deltaG;
    B = fromB + t * deltaB;
    return R,G,B

def R_G_B(s):
    if s < 255: return s,0,0
    len = s // 255
    if len == 1: return 255-(s%255), 0, s%255
    if len == 2: return 0,s%255, 255-(s%255)
    if len == 3: return s% 255,  255, 0
    if len == 4: return  255, 255-(s%255), s% 255
    if len == 5: return 255, s % 255, 255 - (s % 255)
    if len == 6: return 255 - (s % 255), 255,  s % 255
    if len == 7: return s % 255, 255, 255
    if len == 8: return 255 - (s % 255),255 - (s % 255),255 - (s % 255)
    if len >= 9: return 0,0,0
    if  len >= 10: return 255,255,0
colors = ['red', 'blue', 'green', 'grey', 'pink', 'brown', 'yellow', 'lime', 'teal', 'orange']

t = turtle.Pen()
turtle.colormode(255)
t.speed(100000)


turtle.bgcolor('black')
while True:
    s = -1
    n = 0
    for i in range(75):
        if s == 2645: break
        for j in range(i):
            s+=1
            t.color(R_G_B(s))
            t.forward(2)

            t.left(1)
            if s == 2645 : break


turtle.done()