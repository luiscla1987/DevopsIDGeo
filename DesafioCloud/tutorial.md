# Tutorial - Executar programa_desafio1.py em uma instância AWS #

## Criando a Máquina ##
- Acessar o Console de gerenciamento da AWS;
- Acessar os serviços -> EC2;
- Executar instância;
- Procurar por Ubuntu Server - Selecionar 64-bit(x86);
- Escolher o Tipo da instância - t2.micro -> Clicar em _Review and Launch_;
- Clicar em _Launch_;
- Selecionar _Create a ne key pair_;
- Em _Key pair name_ digitar um nome para a chave, ex: **aws-ec2-ubunutu**
- Fazer download da chave arquivo **.pem**;
- Clicar em _Launch Instances_;
- Verificar no Console de instâncias o status da instância criada;
- Definir um nome para a instância - OPCIONAL;

## Acessando a Máquina ##
- No Putty Key Generator, clicar em load e carregar a chave **.pem**;
- Clicar em _save private key_, **salvar o arquivo com extensão .ppk**; 
- Acessar o console da AWS e copiar o **DNS IPv4 público**;
- No _Putty_ em hostname colocar ubuntu@**DNS IPv4 público**;
- Selecionar SSH->Auth e selecionar a chave criada **.ppk** e clicar em _Open_;

## Instalando Requisitos ##
- Com acesso a instância via terminal;

```bash
    sudo apt update
    sudo apt install python3-pip
    sudo pip3 install numpy
    sudo pip3 install scipy
```

## Carregar o Arquivo via SFTP ##
- Configurar novo acesso, no Host utilizar ubuntu@**DNS IPv4 público**;
- Em tipo de logon selecionar **Arquivo Chave**;
- Usuário: **ubuntu**;
- Selecionar o arquivo chave **.ppk** e conectar;
- Criar um diretório e fazer upload do arquivo **programa_desafio1.py** para o diretório criado;

## Executar o Arquivo programa_desafio1.py ##
- Acessar o diretório que tem o arquivo via terminal e executar o comando:

```bash
python3 programa_desafio1.py
```





