# usage:
# python3 <script.py> <fontfile> <width: default=1229>

import sys
import fontforge as ff

if len(sys.argv) > 1:
    glyph_width = 1229
    if len(sys.argv) > 2:
        glyph_width = int(sys.argv[2])
    try:
        font = ff.open(sys.argv[1])
        i = 0
        for glyph in font.glyphs():
            if i == 0:
                print("unicodepoint => glyph width")
                i+=1
            if glyph.width > glyph_width:
                print("{} => {}".format(glyph.codepoint,glyph.width))

    except Exception as e:
        print("Invalid fontfile passed")

else:
    print("please pass fontfile as args")
