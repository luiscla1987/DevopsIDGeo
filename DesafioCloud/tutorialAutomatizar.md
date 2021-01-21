# Executar Automatizada programa_desafio1.py em uma instância AWS #

## Pode ser utilizado Git Actions para automatizar juntamento com AWS, Heroku, Azure, Entre outras; 

- O exemplo foi criado utilizando AWS Lambda Com GitHub Actions e Serverless -> Está no diretório **Automatizar**
- Criar função AWS Lambda usando o _Serverless CLI_
- Precisa adicionar no package.json serverless em devDependecies:
```json
    "devDependencies": {
    "serverless": "^1.67.0",
    "serverless-python-requirements": "^5.1.0"
  }
```
- Adicionar os requisitos python no arquivo _requirements.txt_
- Caso necessite do pacote boto3 ele já vem pré-instalado não precisa adicionar em _requirements.txt_
- Rodar primeiramente o deploy manual:

```bash
    npm run-script deploy
```

- Criar GitHub Actions, criar diretório _.github_ com diretório _workflows_ na raiz do projeto;
- Criar o arquivo _deploy-aws-lambda.yaml_
- Colar esse conteúdo no arquivo:

```yaml
name: deploy-aws-lambda
on:
  push:
    branches:
      - master
jobs:
  deploy:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [10.x]
    steps:
      - uses: actions/checkout@master
      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v1
        with:
          node-version: ${{ matrix.node-version }}
      - name: Install Dependencies
        run: npm install
      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: eu-central-1
      - name: Serverless Deploy
        run: npm run-script deploy
```

- _ AWS_ACCESS_KEY_ID e AWS_SECRET_ACCESS_KEY - Devem ser pegos no console AWS