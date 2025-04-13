from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            base = ord('A') if is_upper else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char  # الأحرف غير الأبجدية تبقى كما هي
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    encrypted_text = ''
    if request.method == 'POST':
        plaintext = request.form['plaintext']
        shift = int(request.form['shift'])
        encrypted_text = caesar_encrypt(plaintext, shift)
    return render_template('index.html', encrypted=encrypted_text)

if __name__ == '__main__':
    app.run(debug=True)
