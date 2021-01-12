import webbrowser
from urllib.parse import urlencode

def refine(string):
    words = string.split(' ')
    if len(words) == 0:
        return ''
    else:
        if string.startswith('show me'):
            return ' '.join(words[2:]).strip(' ')
        else:
            return ' '.join(words[1:]).strip(' ')  # for open and visit command

def predict_website(command):
    print('visiting website>...', end=' ')
    command_orig = command
    command = command.lower().replace(' ', '')
    web_dict = {'youtube': 'youtube.com', 'facebook': 'facebook.com', 'codespeedy': 'codespeedy.com',
                'quora': 'quora.com', 'amazon': 'amazon.in'}
    if command in web_dict.keys():
        website = f'https://www.{web_dict[command]}/'
        print(website)
        webbrowser.open_new(website)
    else:
        q = {'q': command_orig}
        query = urlencode(q)
        complete_url = "https://www.qwant.com/?" + query
        print(complete_url)
        webbrowser.open_new(complete_url)

def main(op_text):
    print('\noperation text:', op_text)
    op_text = op_text.lower()
    if op_text.startswith('visite') or op_text.startswith('montre moi') or op_text.startswith('ouvre') or op_text.startswith('cherche'):  # for visit INTERNET
        if ' ' in op_text:
            new_command = refine(op_text)
            predict_website(new_command)
        else:
            print('\nA Computer cannot visit anything by itself!\n')

if __name__ == '__main__':
    text = 'visit '
    main(text)