#! /usr/bin/env python3

import pandas as pd
import os


class HtmlTable:
    """Creates an 'html' table in sections: 'header', 'columns',
    and 'row'. Functionality is very basic.
    Output is a string of html code, optionally saved to file."""
    def __init__(self, title='Title', width='100', bg_color='rgb(255, 200, 33)'):
        self.title = title
        self.width = str(width)
        self.bg_color = str(bg_color)
        self.alt_bg_color = str(bg_color)

    def table_header(self):
        """Returns the html code for a table header, with title."""
        header = '<table style="background-color: ' \
                + self.bg_color \
                + '; width: 100%"> <caption style="background-color: ' \
                + self.bg_color \
                + '; caption-side: top"><h3>' \
                + self.title + '</h3></caption>'
        return header


def main():
    page = HtmlTable()
    html = page.table_header()
    with open('deleteme.html', 'w') as f:
        f.write(html)
    os.system('epiphany deleteme.html')

if __name__ == '__main__':
    main()
