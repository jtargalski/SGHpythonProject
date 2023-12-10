email1 = 'pawel.rubach@sgh.waw.pl'
email2 = '@sgh.waw.pl'
email3 = 'pawe@sgh.waw.'
email4 = 'pawesgh.waw.'
email5 = 'pawesgh.waw.@.'
email6 = 'pawesgh.waw.@sgh'

email_list = [email1, email2, email3, email4, email5, email6]

def validate_email(email):
    #verify email....
    #email is verified if it fulfills the following conditions
    at_position = email.find('@')
    dot_position_r = email.rfind('.')
    dot_position_l = email.find('.')
    email_length = len(email)

    if at_position < 1:
        return False

    elif dot_position_r == email_length - 1:
        return False

    elif dot_position_l < 1:
        return False

    elif email[at_position + 1] == '.':
        return False

    elif dot_position_r < at_position:
        return False

    else:
        return True

    #then add more conditions to check

for em in email_list:
    print('{}: {}'.format(em, validate_email(em)))