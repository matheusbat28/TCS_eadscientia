# <img src="https://github.com/matheusbat28/TCS/assets/78868039/5ca7f96d-5e80-4369-a240-2dea3779f102" width="100px">

Projeto voltado para educação continuada com intuito conclusão do curso analise e desenvolvimento de sistema (ads)  

# **Como instalar o projeto completo** 🚀

* Primeramente escolhemos onde vamos criar o arquivo 
* Depois acessamos esse local no ternimal do PC e digitamos o seguinte comando: 
~~~
git commit -b back https://github.com/matheusbat28/TCS.git
~~~ 


* Abra o codigo na IDE de sua preferência (IDE usado no projeto VsCode)
* Após abrir crie um venv (gereciado de pacote do python) para criar a venv digite esse comando:

*Comado no linux*
~~~
python3 -m venv venv
~~~

*Comado no window*
~~~
python -m venv venv
~~~

* Comando para iniciar a venv 

*comado no linux*
~~~
. venv/bin/activate
~~~

*Comado no window (PowerShell)*  
*Porém para executar no PowerShell precisa alterar a a politica de execução esse código precisa ser executado no modo de administrador*
~~~
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
~~~
*Para depois tentar iniciar a venv*
~~~
venv\Scripts\Activate.ps1
~~~
*Comado no window (CMD)*
~~~
venv\Scripts\activate.bat
~~~

* Na raiz do projeto tem um arquivo chamado requirements.txt (onde tem todas as dependências do projetos)
* Para baixar as dependências tem que executar esse comando, porém tem q estar na venv
~~~
pip freeze -r requirements.txt
~~~

* Após baixar as dependências tem um arquivo **.env** na raiz do projeto para ter as variaveis de segurança do sistema
* Dentro desse arquivo coloque essa variaveis
~~~
SECRET_KEY = 'django-insecure-8=0$#e#4eig3c2(8li8maxm09(qr0b78t+eamma%0mv6-fuqe$'
DEBUG = True

ALLOWED_HOSTS = ['*']

DB_NAME = 'nome do banco de dado'
DB_USER = 'usuario do banco de dado'
DB_PASSWORD = 'senha do banco dado'
DB_HOST = 'host do banco dado'
DB_PORT = '3306'

RECAPTCHA_PUBLIC_KEY = 'chave publica do recaptcha'
RECAPTCHA_PRIVATE_KEY = 'chave privada do recaptcha'
EMAIL_HOST_USER = 'email que vai ser usado para mandar os email'
EMAIL_HOST_PASSWORD = 'senha do email que manda os email'

EMAIL_RH = 'email do recurso humano'
EMAIL_ADM = 'email da administração'
KEY_YOUTUBE = 'chave da api do google'
~~~
