# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import namedtuple

import lease_application_report_generator


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


Applicant = namedtuple('Applicant', 'sections applicant_name')
Section = namedtuple('Section', 'title type rows')
Row = namedtuple('Row', 'cells')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

bob_summary = Section(
    'Application Summary', 'summary',
    (
        Row(('Property:', 'Sea facing one bedroom Unit at Empire Available 1 September 2020')),
        Row(('Rental amount:', '9500')),
        Row(('Lease start date:', '2021-05-18')),
        Row(('Lease period:', '12 months')),
        Row(('Number of other occupants:', '0')),
        Row(('Tenant name:', 'Jennifer Brewster')),
    )
)

bob_score = Section(
    'Application Score', 'score',
    (
        Row(('Check', 'Score', 'Description')),
        Row(('Affordability 1', '1/1', 'Income is 3x rental amount')),
        Row(('Affordability 2', '2/2', 'Amount on bank statements are confirmed against proof of income for 3 months.')),
        Row(('Credit rating', '2/3', 'Good TPN and no judgements or defaults')),
        Row(('Employment', '1/1', 'Employment confirmed')),
        Row(('Identity', '1/1', 'ID / Passport supplied')),
        Row(('Current/Previous Landlord', '1/1',
            'Landlord reference confirmed that the applicant was a good tenant / paid on time')),
        Row(('Proof of residence', '1/1', 'Proof of residence confirmed')),
        Row(('Total', '9/10', '')),  # Depending on ur module, this could be a tuple of length2
    )
)
bob = Applicant([bob_summary, bob_score], 'Paul Williams')
bill = Applicant([bob_summary, bob_score], 'Susan Boyle')
application = [bill, bob]
lease_application_report_generator.to_pdf(application)
