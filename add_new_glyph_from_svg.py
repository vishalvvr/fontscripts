# usage
# python3 <script.py> <madan.ttf> <madan.svg>
import fontforge as ff
import sys

if len(sys.argv) == 2:
    src_font_file = sys.argv[1]
    src_glyph_svg_name = sys.argv[2]
    output_font_file_name = "madan.sfd"
    glyph_name = 'uni0970'
    glyph_unicode = 0x0970

    try:
        font = ff.open(src_font_file)
        glyph = font.createChar(glyph_unicode, glyph_name)
        glyph.importOutlines(src_glyph_svg_name)

        font.save(output_font_file_name)
    except Exception as e:
        print("Invalid font file/svg provided")
else:
    print("Please pass valid args while executing")