from collections import namedtuple
from fpdf import FPDF

# requirements   - fonts installed
#               - fpdf installed  can use 'pip install fpdf'
#               - namedtuple imported
#               - logo must be in same path as this script
#               - data passed in must be in the applicant, section, row tuple format below

Applicant = namedtuple('Applicant', 'sections applicant_name')
Section = namedtuple('Section', 'title type rows')
Row = namedtuple('Row', 'cells')

LOGO_FILENAME = 'logo.jpg'
BOLD_FONT_PATH = r"C:\Users\Cliftonb\Documents\PyCharmProjects\Faircape Leasing\Roboto-Medium.ttf"  # using relative
# path names searches in a specific folder (see .add_font() docs)
NORMAL_FONT_PATH = r"C:\Users\Cliftonb\Documents\PyCharmProjects\Faircape Leasing\Roboto-Light.ttf"

SUMMARY = 'summary'
SCORE = 'score'


PAGE_WIDTH = 210  # in mm
PAGE_HEIGHT = 297  # in mm
MARGIN = 10  # in mm
IMAGE_WIDTH = 55  # fixed image width
STARTING_Y = 60
SECTION_CELL_HEIGHT = 7
SECTION_HEADER_CELL_HEIGHT = 14
PAGE_HEADER_CELL_HEIGHT = 8
PAGE_SUB_HEADER_CELL_HEIGHT = 6
FULL_BORDER_FLAG = 0  # 0 for NO border, 1 for border (1 doesnt work atm)
CUSTOM_BORDER_FLAG = 'T'
COLUMN_0_WIDTH = 60
COLUMN_1_WIDTH = 20
PAGE_HEADER_FONT_SIZE = 13
PAGE_SUB_HEADER_FONT_SIZE = 8
SECTION_HEADER_FONT_SIZE = 14
SECTION_ROW_FONT_SIZE = 10


def _word_spacing(name):
    out = ""
    for letter in name:
        out += letter + " "
        if letter == " ":
            out += "  "

    return out.strip()


def to_pdf(applications):
    for applicant_num, applicant in enumerate(applications):
        # note this unit (mm) is used in ALL methods except fonts.
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()

        # setup page, colors and fonts
        pdf.set_margins(MARGIN, MARGIN, MARGIN)  # default margins are 10mm
        pdf.set_text_color(0, 0, 0)  # text color to black
        pdf.set_draw_color(154, 166, 157)  # border color to grey
        pdf.add_font('Roboto', '', NORMAL_FONT_PATH, uni=True)
        pdf.add_font('Roboto-Bold', '', BOLD_FONT_PATH, uni=True)

        # setup page header
        pdf.image(LOGO_FILENAME, x=PAGE_WIDTH / 2 - IMAGE_WIDTH / 2, y=MARGIN, w=IMAGE_WIDTH)
        pdf.set_xy(MARGIN, STARTING_Y)
        pdf.set_font('Roboto', '', PAGE_HEADER_FONT_SIZE)  # header font
        pdf.cell(0, h=PAGE_HEADER_CELL_HEIGHT, txt=_word_spacing('LEASE APPLICATION'), border=FULL_BORDER_FLAG, ln=1,
                 align='C')
        pdf.set_font('Roboto', '', PAGE_SUB_HEADER_FONT_SIZE)  # header font
        pdf.cell(0, h=PAGE_SUB_HEADER_CELL_HEIGHT, txt=_word_spacing('- FOR -'), border=FULL_BORDER_FLAG, ln=1,
                 align='C')
        pdf.set_font('Roboto', '', PAGE_HEADER_FONT_SIZE)  # header font
        pdf.cell(0, h=PAGE_HEADER_CELL_HEIGHT, txt=_word_spacing(applicant.applicant_name.upper()),
                 border=FULL_BORDER_FLAG, ln=1, align='C')

        # line between sections
        pdf.ln()

        for section in applicant.sections:
            pdf.set_font('Roboto', '', SECTION_HEADER_FONT_SIZE)  # section header font
            pdf.cell(0, h=SECTION_HEADER_CELL_HEIGHT, txt=section.title, border=FULL_BORDER_FLAG, ln=1, align='L')
            for row_num, row in enumerate(section.rows):
                for col_num, cell in enumerate(row.cells):

                    if section.type == SUMMARY:
                        if col_num == 0:  # row header
                            pdf.set_font('Roboto-Bold', '', SECTION_ROW_FONT_SIZE)  # bold section font
                            pdf.cell(COLUMN_0_WIDTH, h=SECTION_CELL_HEIGHT, txt=cell, border=FULL_BORDER_FLAG, ln=0,
                                     align='L')
                        if col_num == 1:  # row data
                            pdf.set_font('Roboto', '', SECTION_ROW_FONT_SIZE)  # unbold section font
                            pdf.multi_cell(0, h=SECTION_CELL_HEIGHT, txt=cell, border=FULL_BORDER_FLAG, align='L')

                    if section.type == SCORE:
                        if row_num == 0 or row_num == (len(section.rows) - 1):
                            pdf.set_font('Roboto-Bold', '', SECTION_ROW_FONT_SIZE)  # bold section font
                        elif row_num > 0:
                            pdf.set_font('Roboto', '', SECTION_ROW_FONT_SIZE)  # bold section font

                        # second and last row must have top borders
                        if row_num == 1 or row_num == len(section.rows) - 1:
                            if col_num == 0:
                                pdf.cell(COLUMN_0_WIDTH, h=SECTION_CELL_HEIGHT, txt=cell, border=CUSTOM_BORDER_FLAG,
                                         ln=0,
                                         align='L')
                            elif col_num == 1:
                                pdf.cell(COLUMN_1_WIDTH, h=SECTION_CELL_HEIGHT, txt=cell, border=CUSTOM_BORDER_FLAG,
                                         ln=0,
                                         align='L')
                            elif col_num == 2:
                                pdf.multi_cell(0, h=SECTION_CELL_HEIGHT, txt=cell, border=CUSTOM_BORDER_FLAG, align='L')

                        else:
                            if col_num == 0:
                                pdf.cell(COLUMN_0_WIDTH, h=SECTION_CELL_HEIGHT, txt=cell, border=FULL_BORDER_FLAG, ln=0,
                                         align='L')
                            elif col_num == 1:
                                pdf.cell(COLUMN_1_WIDTH, h=SECTION_CELL_HEIGHT, txt=cell, border=FULL_BORDER_FLAG, ln=0,
                                         align='L')
                            elif col_num == 2:
                                pdf.multi_cell(0, h=SECTION_CELL_HEIGHT, txt=cell, border=FULL_BORDER_FLAG, align='L')

            pdf.ln()  # line between sections

        pdf.output(applicant.applicant_name + ' Application Summary' + '.pdf')  # name the file with the application
        # summary title
