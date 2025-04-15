from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired

IDIOMAS_GOOGLE_TRANSLATOR = [
    ('pt', 'Português'), ('en', 'Inglês'), ('es', 'Espanhol'),('af', 'Africâner'), ('sq', 'Albanês'), 
    ('am', 'Amárico'), ('ar', 'Árabe'), ('hy', 'Armênio'), ('az', 'Azerbaijano'), ('eu', 'Basco'), ('be', 'Bielorrusso'),
    ('bn', 'Bengali'), ('bs', 'Bósnio'), ('bg', 'Búlgaro'), ('ca', 'Catalão'),
    ('ceb', 'Cebuano'), ('zh-CN', 'Chinês (Simplificado)'), ('zh-TW', 'Chinês (Tradicional)'),
    ('hr', 'Croata'), ('cs', 'Tcheco'), ('da', 'Dinamarquês'), ('nl', 'Holandês'),
     ('eo', 'Esperanto'), ('et', 'Estoniano'), ('fi', 'Finlandês'),
    ('fr', 'Francês'), ('gl', 'Galego'), ('ka', 'Georgiano'), ('de', 'Alemão'),
    ('el', 'Grego'), ('gu', 'Guzerate'), ('ht', 'Crioulo Haitiano'), ('ha', 'Hauçá'),
    ('haw', 'Havaiano'), ('he', 'Hebraico'), ('hi', 'Hindi'), ('hmn', 'Hmong'),
    ('hu', 'Húngaro'), ('is', 'Islandês'), ('ig', 'Igbo'), ('id', 'Indonésio'),
    ('ga', 'Irlandês'), ('it', 'Italiano'), ('ja', 'Japonês'), ('jv', 'Javanês'),
    ('kn', 'Canarês'), ('kk', 'Cazaque'), ('km', 'Khmer'), ('ko', 'Coreano'),
    ('ku', 'Curdo'), ('ky', 'Quirguiz'), ('lo', 'Lao'), ('la', 'Latim'),
    ('lv', 'Letão'), ('lt', 'Lituano'), ('lb', 'Luxemburguês'), ('mk', 'Macedônio'),
    ('mg', 'Malgaxe'), ('ms', 'Malaio'), ('ml', 'Malaiala'), ('mt', 'Maltês'),
    ('mi', 'Maori'), ('mr', 'Marathi'), ('mn', 'Mongol'), ('my', 'Birmanês'),
    ('ne', 'Nepalês'), ('no', 'Norueguês'), ('ny', 'Chichewa'), ('ps', 'Pachto'),
    ('fa', 'Persa'), ('pl', 'Polonês'),  ('pa', 'Panjabi'),
    ('ro', 'Romeno'), ('ru', 'Russo'), ('sm', 'Samoano'), ('gd', 'Gaélico Escocês'),
    ('sr', 'Sérvio'), ('st', 'Sesoto'), ('sn', 'Shona'), ('sd', 'Sindi'),
    ('si', 'Cingalês'), ('sk', 'Eslovaco'), ('sl', 'Esloveno'), ('so', 'Somali'),
     ('su', 'Sundanês'), ('sw', 'Suaíli'), ('sv', 'Sueco'),
    ('tl', 'Tagalo'), ('tg', 'Tadjique'), ('ta', 'Tâmil'), ('te', 'Telugu'),
    ('th', 'Tailandês'), ('tr', 'Turco'), ('uk', 'Ucraniano'), ('ur', 'Urdu'),
    ('uz', 'Uzbeque'), ('vi', 'Vietnamita'), ('cy', 'Galês'), ('xh', 'Xhosa'),
    ('yi', 'Ídiche'), ('yo', 'Iorubá'), ('zu', 'Zulu')
]

class FormTraduzir(FlaskForm):
    idioma_origem = SelectField('Idioma de origem', choices=IDIOMAS_GOOGLE_TRANSLATOR)
    corpo_traduzir = TextAreaField('Escreva seu Post aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Traduzir')

class FormTraduzido(FlaskForm):
    idioma_destino = SelectField('Idioma de destino', choices=IDIOMAS_GOOGLE_TRANSLATOR)
    corpo_traduzido = TextAreaField('Texto Traduzido')
