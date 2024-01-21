# server.py

from flask import Flask, request, render_template
from ramji import main as m

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    result = ('Jai Shree Ram! Your code is being executed...\n')

    if request.method == 'POST':
        code = request.form.get('code')
            
        try:
            result = m(code)
        except Exception as e:
            result = str(e)


        return render_template('index.html', result=result, ramcode=code)
    return render_template('index.html', result='', ramcode='''JAI_SHRI_RAM

varsha = 1

SADHANA SATYA:
    YADI varsha SAMAAN 14:
        VALMIKI_JI_LIKHO("Raam Ayenge Ayothya")
        RAVAN
    varsha = varsha + 1

SHRI_RAM_JAI_RAM_JAI_JAI_RAM''')

if __name__ == '__main__':
    app.run(debug=True)