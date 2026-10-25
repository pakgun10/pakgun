
from PIL import Image, ImageDraw, ImageFont
W,H = 1200,630
img = Image.new("RGB",(W,H),"#1e293b")
d = ImageDraw.Draw(img)
for x in range(0,W,40): d.line([(x,0),(x,H)],fill="#26334b")
for y in range(0,H,40): d.line([(0,y),(W,y)],fill="#26334b")
# mini bar chart decoration (measured)
bars = [(760,380,90,140),(880,320,90,200),(1000,240,90,280)]
for x,y,w,h in bars:
    d.rectangle([x,y,x+w,y+h], fill="#3b82f6")
    d.line([(x-20,y+h),(x+w+20,y+h)], fill="#64748b", width=3)
def font(sz,bold=False):
    p = "/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if bold else "")
    return ImageFont.truetype(p, sz)
f_badge = font(30, True); f_title = font(52, True); f_sub = font(28)
# badge
bt = "MATEMATIKA / TIKZ"
bw = d.textlength(bt, font=f_badge)
d.rounded_rectangle([60,70,60+bw+40,70+58], radius=12, fill="#f59e0b")
d.text((80,82), bt, font=f_badge, fill="#1e293b")
# title lines, verify right edge < 1150
lines = ["Menggambar Diagram Batang",
         "dengan TikZ:"]
y = 190
for ln in lines:
    w = d.textlength(ln, font=f_title)
    assert 60+w < 1150, (ln, 60+w)
    d.text((60,y), ln, font=f_title, fill="white"); y += 66
sub = ["Ketika Data Kelas Jadi Gambar", "yang Bisa Dipercaya"]
for ln in sub:
    w = d.textlength(ln, font=f_sub)
    assert 60+w < 1150, (ln,60+w)
    d.text((60,y+14), ln, font=f_sub, fill="#f59e0b"); y += 40
img.save('/home/agentuser/.hermes/cache/scratch/pakgun_repo/content/posts/tikz-diagram-batang-data-kelas/featured-image.png')
print("featured ok")
