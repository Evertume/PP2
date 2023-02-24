'''
Given a string, extract all email addresses from it.
For example: Contact us at info@example.com or support@example.org->support@example.org
'''
import re

txt = "Contact us at info@example.com or support@example.org"

def extract_emails(txt):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-z|a-z]{2,}\b'
    emails = re.findall(pattern, txt)
    return list(set(emails))

print(extract_emails(txt))
