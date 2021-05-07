from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Line
from datetime import date

# SET TODAY'S DATE
date = str(date.today().strftime("%m-%d-%Y"))

def main():

    # SETUP REPORTLAB DOCUMENT AS LIST
    document = []

    # ADD LOGO
    document.append(Spacer(1, 20))
    document.append(Image('logo.png', width=8.5 * inch, height=1 * inch))

    # LINES
    horizontal_line = Line(100, 200, 200, 200, strokeWidth=2)

    # COLORS
    GREY = colors.Color(0.74609375, 0.74609375, 0.74609375)  # GREY

    # STYLES
    style_title = ParagraphStyle(name='title',
                                 fontFamily='Calibri',
                                 fontSize=36,
                                 alignment=TA_LEFT,
                                 leftIndent=25
                                 )
    style_main_content = ParagraphStyle(name="main",
                                        fontFamily='Calibri',
                                        fontSize=12,
                                        alignment=TA_LEFT,
                                        leftIndent=75
                                        )
    style_sub_content = ParagraphStyle(name="sub",
                                       fontFamily='Calibri',
                                       fontSize=12,
                                       alignment=TA_LEFT,
                                       leftIndent=100
                                       )
    style_date = ParagraphStyle(name="date",
                                fontFamily='Calibri',
                                fontSize=12,
                                alignment=TA_LEFT,
                                leftIndent=30
                                )
    style_footer = ParagraphStyle(name="footer",
                                  fontFamily='Calibri',
                                  fontSize=12,
                                  alignment=TA_LEFT,
                                  leftIndent=25,
                                  spaceBefore=75
                                  )
    style_sub_footer = ParagraphStyle(name="sub-footer",
                                      fontFamily='Calibri',
                                      fontSize=10,
                                      alignment=TA_LEFT,
                                      leftIndent=50,
                                      rightIndent=100
                                      )
    style_total = ParagraphStyle(name="total",
                                 fontFamily='Calibri',
                                 fontSize=16,
                                 alignment=TA_LEFT,
                                 leftIndent=75
                                 )

    # QUOTE LOGIC
    def ask():
        quote_params = []
        pHours = float(input("How many principle hours? "))
        quote_params.append(pHours)
        aHours = float(input("How many associate hours? "))
        quote_params.append(aHours)
        preEvents = int(input("How many pre-events? "))
        quote_params.append(preEvents)
        eshoot = int(input("Eshoot? "))
        quote_params.append(eshoot)
        album = int(input("How many albums? "))
        quote_params.append(album)
        discount = int(input("Discount percentage: "))
        quote_params.append(discount)
        return quote_params

    def ask_test():
        quote_params = []
        pHours = 3
        quote_params.append(pHours)
        aHours = 0
        quote_params.append(aHours)
        preEvents = 0
        quote_params.append(preEvents)
        eshoot = 1
        quote_params.append(eshoot)
        album = 1
        quote_params.append(album)
        discount = 0
        quote_params.append(discount)
        return quote_params

    def calc(params):
        p_value = params[0] * 165
        a_value = params[1] * 120
        preEv_value = params[2] * 400
        esh_value = params[3] * 350
        alb_value = params[4] * 450
        total = p_value + a_value + preEv_value + esh_value + alb_value
        disc_value = total * params[5] * .01
        if params[5] > 0:
            total = total - disc_value
            params.append(total)
        elif params[5] < 0:
            total = total - disc_value
            params.append(total)
        else:
            params.append(total)
        return params

    def add_title(doc):
        doc.append(Spacer(1, 20))
        doc.append(Paragraph('QUOTE', style_title))
        doc.append(Spacer(1, 30))
        doc.append(Paragraph("Issued: {}".format(date), style_date))
        doc.append(Spacer(1, 40))

        return doc

    def add_quote_content(doc, params):

        # PRINCIPLE PHOTOGRAPHY
        if params[0] is not None and params[0] > 0:
            doc.append(Spacer(1, 20))
            doc.append(Paragraph(
                f'{int(params[0])} Hours Principle Wedding Photography', style_main_content))
        else:
            pass

        # ASSOCIATE PHOTOGRAPHY
        if params[1] is not None and params[1] > 0:
            doc.append(Spacer(1, 5))
            doc.append(Paragraph(
                f'{int(params[1])} Hours Associate Wedding Photography', style_main_content))
        else:
            pass

        # DELIVERABLES
        if params[0] is not None and params[0] > 0:
            if params[0] + params[1] < 5:
                doc.append(Spacer(1, 5))
                doc.append(Paragraph(
                    f'Digital Delivery of Edited Top Shots (150+ Images)', style_sub_content))
            elif params[0] + params[1] >= 5 and params[0] + params[1] < 10:
                doc.append(Spacer(1, 5))
                doc.append(Paragraph(
                    f'Digital Delivery of Edited Top Shots (300+ Images)', style_sub_content))
            elif params[0] + params[1] >= 10 and params[0] + params[1] < 15:
                doc.append(Spacer(1, 5))
                doc.append(Paragraph(
                    f'Digital Delivery of Edited Top Shots (500+ Images)', style_sub_content))
            elif params[0] + params[1] >= 15:
                doc.append(Spacer(1, 5))
                doc.append(Paragraph(
                    f'Digital Delivery of Edited Top Shots (600+ Images)', style_sub_content))
        else:
            pass

        # PRE-EVENTS
        if params[2] is not None and params[2] > 0:
            doc.append(Spacer(1, 20))
            doc.append(Paragraph(
                f'{params[2]} Pre-Event Coverage (3 Hrs Coverage)', style_main_content))
        else:
            pass

        # ENGAGEMENT SHOOT
        if params[3] is not None and params[3] > 0:
            doc.append(Spacer(1, 20))
            doc.append(
                Paragraph(f'{params[3]} Creative Engagement Photoshoot', style_main_content))
            doc.append(Spacer(1, 5))
            doc.append(
                Paragraph(f'2 Hrs Creative Engagement Session', style_sub_content))
            doc.append(Spacer(1, 5))
            doc.append(
                Paragraph(f'Cloud Transfer of Retouched Top Shots', style_sub_content))
        else:
            pass

        # ALBUMS
        if params[4] is not None and params[4] > 0:
            doc.append(Spacer(1, 20))
            doc.append(Paragraph(
                f'{params[4]} 10X10" or 12x9" Premium Layflat Wedding Album (20 Sides)', style_main_content))
        else:
            pass

        # STANDARD ADDITIONS
        doc.append(Spacer(1, 20))
        doc.append(Paragraph(
            f'Complimentary Pre-Wedding Collaboration Sessions', style_main_content))
        doc.append(Spacer(1, 5))
        doc.append(Paragraph(
            f'Complimentary Online Cloud Hosted Album (1 Year)', style_main_content))

        # DISCOUNT
        if params[5] is not None and params[5] > 0:
            doc.append(Spacer(1, 20))
            doc.append(Paragraph(f'{params[5]}% Discount', style_main_content))
        elif params[5] is not None and params[5] < 0:
            pass
        else:
            pass

        # TOTAL
        doc.append(Spacer(1, 30))
        doc.append(Paragraph('TOTAL: ${:.2f}'.format(params[6]), style_total))

        return doc

    def add_quote_footer(doc):
        doc.append(Spacer(1, 40))
        doc.append(Paragraph(f'Quote Regulations:', style_footer))
        doc.append(Spacer(1, 10))
        doc.append(Paragraph(
            f'1) This quote is not a mutually binding agreement and as such, will not be treated as one.', style_sub_footer))
        doc.append(Spacer(1, 5))
        doc.append(Paragraph(f'2) This document is by nature a private document, not to be shared externally. It is meant as a \n guideline between The Company & The Client.', style_sub_footer))
        doc.append(Spacer(1, 5))
        doc.append(Paragraph(
            f'3) This quote is not inclusive of local sales, goods, or harmonized tax.', style_sub_footer))
        doc.append(Spacer(1, 5))
        doc.append(Paragraph(
            f'4) This quote is inclusive of travel and accommodation unless otherwise stipulated herein or \n on the forthcoming contract.', style_sub_footer))

        return doc

    def add_lines(doc):
        doc.append(horizontal_line)

        return doc

    # CREATES LIST FROM CALCULATIONS
    params = calc(ask())

    # CREATES FINAL DOCUMENT
    SimpleDocTemplate('Quote.pdf', pagesize=letter,
                      rightMargin=30, leftMargin=30,
                      topMargin=30, bottomMargin=30).build(add_quote_footer(add_quote_content(add_title(document), params)))


if __name__ == '__main__':
    main()
