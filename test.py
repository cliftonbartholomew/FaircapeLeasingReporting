from collections import namedtuple
from fpdf import FPDF


HEAD = 'head'
DATA = 'data'
PAGEWIDTH = 210 #in mm
PAGEHEIGHT = 297 #in mm
MARGIN = 10 #in mm
IMAGE_WIDTH = 80
STARTING_Y = 90 #need to rethink this

Applicant = namedtuple('Applicant', 'sections')
Section = namedtuple('Section', 'title rows')
Row = namedtuple('Row', 'style cells')

bob_summary = Section(
    'Application Summary', #type here ('summary' or 'score')
    (
        Row(HEAD, ('Porperty:', 'Sea facing 1 bedroom')),
        Row(DATA, ('Rental Amount', '9500')),
        Row(DATA, ('What happended to ur bday', '2021-05-18')),
    )
)

bob_score = Section(
    'Application Score',
    (
        Row(HEAD, ('Check', 'Score', 'Description')),
        Row(DATA, ('Affordability 1', '1/1', 'Income 3x Rental')),
        Row(DATA, ('Affordability 2', '2/2', 'Amount on bank is lekker')),
        Row(HEAD, ('Total', '3/3', '')),  # Depending on ur module, this could be a tuple of length2
    )
)
bob = Applicant((bob_summary, bob_score))
bill = bob  # In reality would be diff data
application = [bill, bob]

#note this unit is used in ALL methods except fonts.
#also, the default margins are 10mm
pdf = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
pdf.set_margins(MARGIN,MARGIN,MARGIN)
pdf.add_page()
pdf.set_text_color(0, 0, 0)
pdf.set_draw_color(113, 116, 122)

#to autosize the logo
pdf.image('logo.jpg', x = PAGEWIDTH/2-IMAGE_WIDTH/2, y = MARGIN, w = IMAGE_WIDTH)

pdf.set_xy(MARGIN, STARTING_Y)

#Application section
pdf.set_font('Arial', 'B', 18)
pdf.cell(PAGEWIDTH/2 - MARGIN - 30, h = 14, txt = application[0].sections[0].title, border=0, ln = 1, align = 'L')

pdf.set_font('Arial', 'B', 14)
pdf.cell(PAGEWIDTH/2 - MARGIN - 30, h = 10, txt = application[0].sections[0].rows[0].cells[0], border=1, ln = 0, align = 'L')
pdf.set_font('Arial', '', 14)
pdf.cell(PAGEWIDTH/2 - MARGIN + 30, h = 10, txt = application[0].sections[0].rows[0].cells[1], border=1, ln = 1, align = 'L')
pdf.set_font('Arial', 'B', 14)
pdf.cell(PAGEWIDTH/2 - MARGIN - 30, h = 10, txt = application[0].sections[0].rows[1].cells[0], border=1, ln = 0, align = 'L')
pdf.set_font('Arial', '', 14)
pdf.cell(PAGEWIDTH/2 - MARGIN + 30, h = 10, txt = application[0].sections[0].rows[1].cells[1], border=1, ln = 1, align = 'L')

pdf.ln()


#score section
pdf.set_font('Arial', 'B', 18)
pdf.cell(PAGEWIDTH/2 - MARGIN, h = 14, txt = application[0].sections[1].title, border=0, ln = 1, align = 'L')

pdf.set_font('Arial', 'B', 14)
pdf.cell(PAGEWIDTH/3 - (MARGIN*2/3) +15, h = 10, txt = application[0].sections[1].rows[0].cells[0], border=1, ln = 0, align = 'L')
pdf.cell(PAGEWIDTH/3 - (MARGIN*2/3) -30, h = 10, txt = application[0].sections[1].rows[0].cells[1], border=1, ln = 0, align = 'L')
pdf.cell(PAGEWIDTH/3 - (MARGIN*2/3) +15, h = 10, txt = application[0].sections[1].rows[0].cells[2], border=1, ln = 1, align = 'L')

pdf.set_font('Arial', '', 14)
pdf.cell(PAGEWIDTH/3 - (MARGIN*2/3) +15, h = 10, txt = application[0].sections[1].rows[1].cells[0], border=1, ln = 0, align = 'L')
pdf.cell(PAGEWIDTH/3 - (MARGIN*2/3) -30, h = 10, txt = application[0].sections[1].rows[1].cells[1], border=1, ln = 0, align = 'L')
pdf.cell(PAGEWIDTH/3 - (MARGIN*2/3) +15, h = 10, txt = application[0].sections[1].rows[1].cells[2], border=1, ln = 1, align = 'L')

pdf.cell(PAGEWIDTH/3 - (MARGIN*2/3) +15, h = 10, txt = application[0].sections[1].rows[2].cells[0], border=1, ln = 0, align = 'L')
pdf.cell(PAGEWIDTH/3 - (MARGIN*2/3) -30, h = 10, txt = application[0].sections[1].rows[2].cells[1], border=1, ln = 0, align = 'L')
pdf.cell(PAGEWIDTH/3 - (MARGIN*2/3) +15, h = 10, txt = application[0].sections[1].rows[2].cells[2], border=1, ln = 1, align = 'L')

#if last row, bold and two columns
pdf.set_font('Arial', 'B', 14)
pdf.cell(PAGEWIDTH/3 - (MARGIN*2/3) +15, h = 10, txt = application[0].sections[1].rows[3].cells[0], border=1, ln = 0, align = 'L')
pdf.cell(PAGEWIDTH/3 - (MARGIN*2/3) -30, h = 10, txt = application[0].sections[1].rows[3].cells[1], border=1, ln = 0, align = 'L')


pdf.output('Automated PDF Report.pdf')



