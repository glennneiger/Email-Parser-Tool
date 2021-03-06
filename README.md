# Email Parser Tool
Accesses an email account through the imap or smtp gmail servers and parses the data

# What you need to know
Python 3.7. This uses the imaplib and email libraries. 

Things you will need:
  - gmail account
  - gmail account app password
  - the desired mail server, either smtp.gmail.com or imap.gmail.com
  - a specific FROM_CONDITION, which is just a string condition equal to the email 
      address you are receiving from
  - a specific SUBJECT_CONDITION, which is just 2 special characters that are looked for 
      at the beginning of an email's subject field. 
      
      Example: '#>New Client'
      
      In the above example, the 2 special characters are '#>'. The emails that you are trying to open 
      would need to have those characters as the first 2 characters in the subject field of the email. 
      This is to avoid opening unwanted emails.

The parse_and_commit() method will most likely need to be modified to your application. You can 
then add your own logic for adding data to your database.

If you want to use this in script form and not in a project, simply add in your parameters 
into params.txt and run directly from email_parser_tool.py
  
