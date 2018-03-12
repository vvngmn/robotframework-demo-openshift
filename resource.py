url="https://host-8-241-25.host.centralci.eng.rdu2.redhat.com:8443"
user1='xiaocwan'
password1="p"
def random_id(length):
    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    name = ''
    for i in range(0,length,2):
        name += random.choice(number)
        name += random.choice(alpha)
    return name
