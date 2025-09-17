from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

from app import db, bcrypt
from app.models import Contato, User

class UserForm(FlaskForm):
    nome= StringField("Nome", validators=[DataRequired(), Length(max=50)])
    sobrenome= StringField("Sobrenome", validators=[DataRequired(), Length(max=50)])
    email= StringField("Email", validators=[DataRequired(), Email()])
    senha= StringField("senha", validators=[DataRequired()])
    confirmaçao_senha = PasswordField("Confirme sua senha", validators = [DataRequired(),EqualTo("senha")])
    btnSubmit = SubmitField("Cadastrar")
    
def validate_email(self, email):
    if User.query.filter_by(email=email.data).first():
        raise ValidationError("Usuario ja cadastrado com esse email!!!")
def save(self):
    hashed_senha = bcrypt.generate_password_hash(self.senha.data.encode("utf-8"))
    user = User(
        nome = self.nome.data,
        sobrenome= self.sobrenome.data,
        email= self.email.data,
        senha=hashed_senha
        
    )
    db.session.add(user)
    db.session.commit()
    return user

class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email()])
    senha = PasswordField("senha", validators=[DataRequired()])
    btnSubmit = SubmitField("login")
    def login(self):
        user = User.query.filter_by(email = self.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.senha, self.senha.data.encode("utf-8")):
                return user
            else:
                raise Exception("senha incorreta")
        else:
            raise Exception("usuario nao encontrado")
    

class ContatoForm(FlaskForm):
    nome= StringField("Nome", validators=[DataRequired(), Length(max=50)])
    email= StringField("Email", validators=[DataRequired()])
    assunto= StringField("Assunto", validators=[DataRequired(), Length(max=100)])
    mensagem= StringField("Mensagem", validators=[DataRequired(), Length(max=500)])
    btnSubmit= SubmitField("Enviar")

    def save(self):
        contato = Contato(
            nome= self.nome.data,
            email= self.email.data,
            assunto= self.assunto.data,
            mensagem = self.mensagem.data
        )
        db.session.add(contato)
        db.session.commit()