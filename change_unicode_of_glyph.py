# usage:
# python3 <script.py> <fontfile>

import sys
import fontforge as ff

glyph_name = "uni0970"
glyph_unicode = 0x0970

if len(sys.argv) > 1:
    try:
        font = ff.open(sys.argv[1])

        for glyph in font.glyphs():
            if glyph.glyphname == glyph_name:
                glyph.unicode = glyph_unicode 
                print(glyph.glyphname)

        font.save("madan1.ttf")

    except Exception as e:
        print("Invalid fontfile passed")

else:
    print("please pass fontfile as args")
