from flask import Flask, render_template, url_for, request
from translator import app
from translator.forms import FormTraduzir, FormTraduzido
from deep_translator import GoogleTranslator


@app.route('/', methods=['GET', 'POST'])
def home():
    form_traduzir = FormTraduzir()
    form_traduzido = FormTraduzido()
    
    if form_traduzir.validate_on_submit() and 'botao_submit' in request.form:
        idioma_traduzir = form_traduzir.idioma_origem.data
        idioma_traduzido = form_traduzido.idioma_destino.data
        tradutor = GoogleTranslator(source=idioma_traduzir, target=idioma_traduzido)
        texto = form_traduzir.corpo_traduzir.data
        traducao = tradutor.translate(texto)
        form_traduzido.corpo_traduzido.data = traducao
    return render_template('home.html', form_traduzido=form_traduzido, form_traduzir=form_traduzir)