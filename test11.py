import os
from icecream import ic
import fitz
gst_key_words={ #### GST #####
                 "GST Payment Challan/Receipt": "goods and services tax payment receipt",
                 "Under_GST Payment Challan/Receipt" : "debit advice",
                 "GSTR-1": "form gstr-1",
                 "GSTR-3B": "form gstr-3b",
                 "GSTR-9": "form gstr-9",
                 "GSTR-9C": "form gstr-9c",
                 "LUT": "acknowledgment for lut",
                 "Under_LUT": "form gst rfd - 11",
                 "REG-02 for REG-16": "form gst reg-02",
                 "Registration": "form gst reg-06",
               #### IT ####
                 "IT_PAN"                      : "permanent account number",
                 "IT_TDS_PAYMENT"              : "taxpayer's counterfoil",
                 "IT_UNDER_TDS_PAYMENT"        : "nsdl direct taxes",
                 "IT_AADHAR"                   : "unique identification authority of india",
                 "IT_TRANSFER_PRICING_AUDIT"   : "form no. 3ceb",
                 "IT_FORM_16A"                 : "form no. 16a",
                 "IT_TAN"                      : "tax deduction account number (TAN)",
                 #"IT_TAN2"                     : "tan",
                 "IT_TAX_AUDIT_REPORT"          : "form no.3ca",
                 "IT_TAX_AUDIT_REPORT2"         : "form no.3cd",
                 "IT_FORM_16"                   : "form no.16",
                 "IT_IT_RETURN"                 : "indian income tax return acknowledgement",
                 "IT_IT_RETURN2"                : "statement of income",
                 "IT_IT_RETURN3"                : "itr-6",
                 "IT_IT_RETURN4"                : "itr-2",
                 "IT_TCS_RETURN"                : "statement of tcs under section 206c of the income-tax act,1961",
                 "IT_TCS_RETURN2"               : "sam hash000000000000000",
                 "IT_TDS_RETURN"                : "form no. 27a",
                 "IT_TDS_RETURN2"               : "statement of tds under section 200(3) of the income-tax act",
                 "IT_TDS_RETURN3"               : "type of payment : 94j-fees for professional or technical services",
                 "IT_TDS_RETURN4"               : "acknowledgement receipt of",
                 "IT_TDS_RETURN5"               : "type of payment : 94C-payment of contractors and sub-contractors"

               }
#gst_key_words_values= list(gst_key_words.values())
#ic(gst_key_words_values,type(gst_key_words_values))
def data_validity_check(file_path):
    try:
        file_name, file_extension= os.path.splitext(file_path)
        ic(file_name,file_extension)

        if (file_extension==".pdf") or (file_extension==".PDF"):
            doc = fitz.open(file_path)
            page_font_count = len(doc.get_page_fonts(0))
            ic(doc.get_page_fonts(0))
            ic(page_font_count)
            if page_font_count > 1:
                ic("Its a digital pdf")
            else:
                ic("Its a scanned pdf")
                return "Relevant_document"

            # Load your PDF
            import pdfplumber
            import difflib as dl
            with pdfplumber.open(file_path) as pdf:
                # ic(pdf.chars)
                first_page = pdf.pages[0].extract_text()[:500].lower()
                # ic(first_page,type(first_page))
                for value in gst_key_words.values():
                    if value in first_page:
                        return "Related_document"

                for value in gst_key_words.values():
                    close_match= dl.get_close_matches(value,first_page.split("\n"),cutoff=0.7,n=1)
                    ic(close_match)
                    if len(close_match)>0:
                        return "Related_document"

                return "Irrelavent_document"

        elif file_extension in (".jpeg",".jpg",".png",".tiff"):
             return "Related_document"
        elif file_extension in (".docx"):
             return "Related_document"
    except Exception as e:
        ic(e)
        return "Irrelavent_document"

check = data_validity_check("E:/techweirdo/AI Training Docs/Income Tax/Form 16A/AAAAJ4129L_Q2_2020-21.pdf")
ic(check)