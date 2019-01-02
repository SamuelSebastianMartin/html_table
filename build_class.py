#! /usr/bin/env python3



class HtmlTable:
    """Creates an 'html' table in sections: 'header', 'columns',
    and 'row'. Functionality is very basic.
    Output is a string of html code, optionally saved to file."""
    def __init__(self, title='Title', width='100', bg_color='rgb(255, 200, 33)'):
        self.title = title
        self.width = str(width)
        self.bg_color = str(bg_color)
        self.alt_bg_color = str(bg_color)
        self.saveas = 'html_table.html'
        self.page = []

    def table_header(self):
        """Returns the html code for a table header, with title."""
        header = '<table style="background-color: ' \
                + self.bg_color \
                + '; width: 100%"> <caption style="background-color: ' \
                + self.bg_color \
                + '; caption-side: top"><h3>' \
                + self.title + '</h3></caption>'
        self.page.append(header)
        return header

    def table_columns(self):
        columns = '<colgroup>\
            <col style="background-color: ' + self.bg_color + '">,\
            <col style="background-color: ' + self.alt_bg_color + '">\
            <col style="background-color: ' + self.bg_color + '">\
                </colgroup>'
        self.page.append(columns)
        return columns

    def column_headings(self, td1='One', td2='Two', td3='Three'):
        col_head = '<tr align="center">\
                        <th scope="col">' + td1 + '</th>\
                        <th scope="col">' + td2 + '</th>\
                        <th scope="col">' + td3 + '</th>\
                    </tr>'
        self.page.append(col_head)
        return col_head

    def add_row(self, entry1='entry', entry2='entry', entry3='entry'):
        row = '<tr align="center">\
                    <td>' + entry1 + '</td>\
                    <td>' + entry2 + '</td>\
                    <td>' + entry3 + '</td>\
                </tr>'
        self.page.append(row)
        return row

    def write_page(self):
        full_page = ''.join(self.page)
        with open(self.saveas, 'w') as f:
            f.write(full_page)


def test_HtmlTable():
    """Builds a dummy table using all the class functionality, and opens
    the table in a browser to test.
    The 'os.system()' call should be adjusted for your own OS and browser."""
    import os

    page = HtmlTable()
    header = page.table_header()
    page.alt_bg_color = "rgb(235, 180, 33"
    columns = page.table_columns()
    col_head = page.column_headings('Term 1', 'Term 2', 'Term 3')
    row1 = page.add_row()
    row2 = page.add_row()
    row3 = page.add_row()
    page.write_page()
    os.system('epiphany deleteme.html')

if __name__ == '__main__':
    test_HtmlTable()
