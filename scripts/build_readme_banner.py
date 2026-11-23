from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Assets" / "readme"
OUT.mkdir(parents=True, exist_ok=True)
W, H = 1280, 640
BG = (22, 24, 23)
PAPER = (236, 224, 201)
MUTED = (161, 152, 135)
GOLD = (205, 164, 95)
FAINT = (84, 79, 70)

def load_mono(size, bold=False):
    candidates = [
        r"C:\Windows\Fonts\consolab.ttf" if bold else r"C:\Windows\Fonts\consola.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationMono-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationMono-Regular.ttf",
        "/System/Library/Fonts/Menlo.ttc",
    ]
    for candidate in candidates:
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


tiny = load_mono(14)
small = load_mono(16)
body = load_mono(18)
block = load_mono(20, bold=True)

GLYPHS = {
    "S": ["#####", "#....", "#....", "#####", "....#", "....#", "#####"],
    "C": ["#####", "#....", "#....", "#....", "#....", "#....", "#####"],
    "R": ["####.", "#...#", "#...#", "####.", "#.#..", "#..#.", "#...#"],
    "I": ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "#####"],
    "B": ["####.", "#...#", "#...#", "####.", "#...#", "#...#", "####."],
    "E": ["#####", "#....", "#....", "####.", "#....", "#....", "#####"],
}

# The line drawing is literal ASCII: a sheet, typewriter body, keys, carriage,
# and a coffee cup. Two lines are animated as if they are being typed.
scene = [
    "                         .-----------------------------------------------.",
    "                        /  ________________________________             /|",
    "                       /  |                                |           / |",
    "                      /   |                                |          /  |",
    "                     /    |                                |         /   |",
    "                    /     |                                |        /    |",
    "                   /      |                                |       /     |",
    "                  /       |                                |      /      |",
    "                 /        |                                |     /       |",
    "                /         |                                |    /        |",
    "               /__________|________________________________|___/         |",
    "               |         .------------------------------------.           |",
    "               |        /  S C R I B E  /  WRITING PRACTICE  \\          |",
    "               |       /______________________________________\\         |",
    "               |       |   []  []  []  []  []  []  []  []    |         |",
    "               |       |  []  []  []  []  []  []  []  []     |         |",
    "               |       |    []  []  []  []  []  []  []       |         |",
    "               |       |____________________________________|         |",
    "               |      /  []  []  []  []  []  []  []  []      \\        |",
    "               |     /________________________________________\\       |",
    "               |        ||      ||      ||      ||      ||              |",
    "               `--------||------||------||------||------||-------------'",
    "                        `--------------------------------'",
    "                           \\________________________/",
    "                           /__________________________\\",
    "                              / / / / / / / / / /",
    "                 ( (       .------------------.       / / /",
    "                  ) )      |  SLOW  /  SURE   |      / /",
    "                .-----.    `------------------'     / /",
    "                |     |                             / /",
    "                `-----'                            '-'",
]

paper_lines = [
    "1:1  In the name of GOD,",
    "     Most Gracious, Most",
    "     Merciful.",
    "1:2  Praise be to GOD,",
    "     Lord of the universe.",
]

def base_frame():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.text((38, 20), "+" + "=" * 135 + "+", font=tiny, fill=FAINT)
    d.text((58, 43), "WIKISUBMISSION  /  QURAN COPYING PRACTICE", font=tiny, fill=MUTED)
    d.text((1004, 43), "VERSE BY VERSE  /  NO. 01", font=tiny, fill=GOLD)
    d.text((38, 68), "+" + "-" * 135 + "+", font=tiny, fill=FAINT)

    # Large ASCII title on the left.
    x0, y0, cw, ch, gap = 54, 119, 12, 21, 1
    for row in range(7):
        x = x0
        for letter in "SCRIBE":
            for col, on in enumerate(GLYPHS[letter][row]):
                if on == "#":
                    d.text((x + col * cw, y0 + row * ch), "#", font=block, fill=PAPER)
            x += 5 * cw + cw + gap

    d.text((58, 294), "THE ART OF ATTENTIVE WRITING", font=small, fill=GOLD)
    d.text((58, 328), "Copy one verse at a time.", font=body, fill=PAPER)
    d.text((58, 358), "Let every word pass through your hands.", font=small, fill=PAPER)
    d.text((58, 414), "6,346 TYPING ENTRIES", font=tiny, fill=MUTED)
    d.text((58, 474), "[ TYPE ]  [ PAUSE ]  [ CONTINUE ]", font=tiny, fill=GOLD)
    d.text((58, 505), "Progress saved as you go.", font=tiny, fill=MUTED)
    d.text((58, 559), "ONE VERSE AT A TIME", font=tiny, fill=PAPER)

    # Typewriter scene appears as a block of detailed ASCII line art.
    for i, line in enumerate(scene):
        d.text((535, 95 + i * 16), line, font=tiny, fill=PAPER)

    d.text((38, 594), "+" + "-" * 135 + "+", font=tiny, fill=FAINT)
    d.text((58, 615), "[=====================>........................]", font=tiny, fill=GOLD)
    d.text((510, 615), "A QUIET PRACTICE  /  FROM FIRST VERSE TO LAST", font=tiny, fill=MUTED)
    d.text((38, 631), "+" + "=" * 135 + "+", font=tiny, fill=FAINT)
    return im, d


frames = []
steps = 80
for frame_no in range(steps):
    im, d = base_frame()
    # Reveal each verse line by line, then blink the ASCII cursor.
    frames_per_line = 14
    for line_no, line in enumerate(paper_lines):
        start = 5 + line_no * frames_per_line
        count = max(0, min(len(line), (frame_no - start) * 2))
        if count:
            typed = line[:count]
            cursor = "_" if frame_no % 2 == 0 else " "
            d.text((752, 130 + line_no * 17), typed + cursor, font=tiny, fill=GOLD)
    frames.append(im)

gif_path = OUT / "scribe-ascii-cover.gif"
png_path = OUT / "scribe-ascii-cover.png"
frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=100,
               loop=0, optimize=True, disposal=2)
frames[-1].save(png_path, optimize=True)

print(gif_path)
print(png_path)
