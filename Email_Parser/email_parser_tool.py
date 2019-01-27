import imaplib
import email


class EmailParserTool:
    def __init__(self, domain, username, password, server, from_condition,
                 subject_condition, email_state):
        """
        These are the settings for the email account and email grabbing conditions.

        :param domain: The domain name, such as '@gmail.com'
        :param username: The username of the email before the '@' symbol.
        :param password: The password for the account. Probably will need to setup an
            app password so outside parties can connect.
        :param server: Use either 'smtp.gmail.com' or 'imap.gmail.com'
        :param from_condition: This is used to make sure only emails are opened from a certain
            sender.
        :param subject_condition: This is used to make sure only emails are opened with a specific 2
            special characters at beginning of subject. Prevents unwanted emails from being
            opened. Idea is that this overall model will be used to only extract specific emails
        :param email_state: Enter 'ALL' for all emails, or 'UNSEEN' to view unread emails
        :param mail: Mail object used for logging and fetching emails
        """

        self.domain = domain
        self.username = username + self.domain
        self.password = password
        self.server = server
        self.from_condition = from_condition
        self.subject_condition = subject_condition
        self.email_state = email_state
        # Leave self.mail alone
        self.mail = None

    def connect(self):
        """
        Connects to email account.
        """

        self.mail = imaplib.IMAP4_SSL(self.server)
        self.mail.login(self.username, self.password)

    def get_messages(self):
        """
        Mail object first selects the email account's inbox. Then looks for emails based
        on the desired EMAIL_STATE. If status is OK, mail object fetches the emails in the
        desired state. If emails meet the FROM and SUBJECT CONDITIONS, they are opened and
        sent to the parse_and_commit() method. After work load is complete, mail object
        closes the connection.
        """

        # Select inbox and get all messages
        self.mail.select('INBOX')
        status, messages = self.mail.search(None, self.email_state)

        if status == 'OK':
            for msg_num in messages[0].split():
                typ, data = self.mail.fetch(msg_num, '(RFC822)')
                for raw_msg in data:
                    if isinstance(raw_msg, tuple):
                        new_email = email.message_from_bytes(raw_msg[1])
                        if self.from_condition in new_email['From']:
                            if new_email['Subject'][0:2] == self.subject_condition:
                                msg = new_email.get_payload()
                                self.parse_and_commit(msg)

        self.mail.close()

    def parse_and_commit(self, email_):
        """
        After email has been found and contents extracted, email is split by each new line.
        Each line is then placed into appropriate variable. This will need to be adjusted per
        application.
        """

        # Email contents are split by each new line
        formatted_email = email_.splitlines()

        # Individual email content lines are accessed by index and placed in variable
        loan_type = formatted_email[0]
        business_name = formatted_email[1]
        business_class = formatted_email[2]
        first_name = formatted_email[4].split(' ')[0]
        last_name = formatted_email[4].split(' ')[1]
        email = formatted_email[5]
        business_phone = formatted_email[6]
        mobile_phone = formatted_email[7]
        zip_code = formatted_email[8]
        business_type = formatted_email[10]
        loan_option = formatted_email[13]
        loan_amount = formatted_email[14]
        avg_monthly_income = formatted_email[16]
        credit_score = formatted_email[17]
        retirement = formatted_email[18]
        company_type = formatted_email[20]
        business_length = formatted_email[21]
        company_website = formatted_email[22]
        physical_biz_location = formatted_email[23]
        business_plan = formatted_email[24]

        # Add logic for adding data to your database
