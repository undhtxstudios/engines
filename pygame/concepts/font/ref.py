"""
font module: loading and rendering fonts

pygame.font.init()
    automatically called by pygame.init()
  
pygame.font.quit():
    automatically called by pygame.quit()

pygame.font.get_init()
    check font module is initialized

pygame.font.get_default_font()
    returns the filename of the default font, typically freesansbold.ttf

pygame.font.get_fonts()
    returns a list of all available system fonts in lowercase with spaces and punctuation removed

pygame.font.match_font(name, bold=False, italic=False)
    finds and returns the path to a specific font on the system

pygame.font.SysFont(name, size, bold=False, italic=False)
    creates a Font object from the system fonts

Font Class

pygame.font.Font(file_path=None, size=12)
    creates a new Font object from a file
    if file_path is None, the default font is used
    the size parameter specifies the font size in pixels.

Attributes
bold: gets or sets whether the font should be rendered in (faked) bold
italic: gets or sets whether the font should be rendered in (faked) italics
underline: gets or sets whether the font should be rendered with an underline
strikethrough: gets or sets whether the font should be rendered with a strikethrough


render(text, antialias, color, background=None)
    renders text onto a new surface

size(text): returns the width and height required to render the specified text.
metrics(text): returns a list of tuples with metrics for each character in the text (minx, maxx, miny, maxy, advance).
get_linesize(): returns the line space in pixels for the font text.
get_height(): returns the height in pixels of the rendered text.
get_ascent(): returns the ascent height in pixels from the baseline to the top of the font.
get_descent(): returns the descent height in pixels from the baseline to the bottom of the font.

set_bold(bool): enables or disables bold rendering.
get_bold(): checks if the font is rendered in bold.
set_italic(bool): enables or disables italic rendering.
get_italic(): checks if the font is rendered in italic.
set_underline(bool): enables or disables underlining.
get_underline(): checks if the font is rendered with an underline.
set_strikethrough(bool): enables or disables strikethrough rendering.
get_strikethrough(): checks if the font is rendered with a strikethrough.
"""