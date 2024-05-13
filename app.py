# python -m venv kerol
# kerol\Scripts\activate
# pip install flask
# pip install scikit-learn -> para reconhecer o pickle onde faz o tratamento para o ML


from flask import Flask, request, render_template
from warnings import filterwarnings
import pickle

filterwarnings('ignore')

def import_model(): # abre o modelo treinado
    modelo = pickle.load(open('./modelo.sav','rb'))
    return modelo

modelo = import_model()
app = Flask(__name__)

@app.route('/') #importando o template
def index():
    return render_template('forms.html')

@app.route('/predict',methods=['POST']) #mandando seus dados
def predict():
     
    parametros = [float(request.form['Grávidez']), float(request.form['Glicose']), float(request.form['Pressão_Sanguinea']), float(request.form['Insulina']), float(request.form['BMI']), float(request.form['Idade'])]
    
    resultado = modelo.predict([ parametros ])[0]
    
    if resultado == 0: 
        resultado = 'Não há chances de Diabetes'
    else:
        resultado = 'Há chances de Diabetes'


    return f'Seu resultado é : "{resultado}"!'



app.run(
    debug=True,
    port='5000'
)
