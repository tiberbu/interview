
import re

def mask_dates_and_emails(input_string):
    
    date_pattern = r'\b(\d{2}/\d{2}/\d{2})\b' 

   
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    date_mask = '**/**/**'  
    email_mask = '*****@*****.***'  

    
    masked_string = re.sub(date_pattern, date_mask, input_string)

    
    masked_string = re.sub(email_pattern, email_mask, masked_string)

    return masked_string




