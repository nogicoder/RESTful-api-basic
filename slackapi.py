import requests


method_list = ['conversations.history', 'channels.list', 'chat.postEphemeral', 'chat.postMessage', 'chat.meMessage']


def get_input():
    file = open('input.txt')
    for line in file:
        if line.startswith('METHOD'):
            method = line[6:].strip()
        elif line.startswith('URL'):
            url = line[4:].strip()
        elif line.startswith('APIMethod'):
            url += line[10:].strip()
        elif line.startswith('PARAM'):
            params = line[6:].strip().replace(',','&')
            url = url + params
        elif line.startswith('q'):
            q = line[2:]
    file.close()
    return method, url


def get_value():
    method, url = get_input()
    print(url)
    r = requests.get(url=url)
    data = r.json()
    with open('output.txt', 'w+') as file:
        file.write(r.text)

if __name__ == '__main__':
    get_value()
