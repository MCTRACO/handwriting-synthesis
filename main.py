from hand import Hand
from textwrap import wrap
import unicodedata


def remove_accents(input_string):
    # Normalize the string to decomposed Unicode form
    normalized = unicodedata.normalize('NFD', input_string)
    # Filter out combining diacritic marks and return the result
    result = ''.join(c for c in normalized if unicodedata.category(c) != 'Mn')
    return result


hand = Hand()


def write_text(text, filename, style=3, bias=2.5, color="black", width=1, linelength=70):
    new_text = remove_accents(text)
    lines = wrap(new_text, linelength)
    biases = [bias for i in lines]
    styles = [style for i in lines]
    stroke_colors = [color for i in lines]
    stroke_widths = [width for i in lines]

    hand.write(
        filename=f'{filename}.svg',
        lines=lines,
        biases=biases,
        styles=styles,
        stroke_colors=stroke_colors,
        stroke_widths=stroke_widths
    )

