# 🌐 Redirecionador de Webhook

Este projeto é um redirecionador de webhooks desenvolvido em Python utilizando o Flask. Ele recebe requisições de webhooks, processa os dados e os redireciona para uma URL de destino específica.

## 📋 Funcionalidades

- Recebe requisições de webhooks na rota `/api/webhooks/incoming/omie/<webhook_id>`.
- Processa os dados recebidos e extrai o campo `topic`, se presente.
- Redireciona os dados para uma URL de destino configurada.
- Registra logs detalhados das requisições e respostas.

## 🚀 Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório.
3. Instale as dependências necessárias:
    ```sh
    pip install flask requests
    ```
4. Para desenvolvimento local, execute o aplicativo com o servidor Flask sem debug:
    ```sh
    python WebhookRediGlobal.py
    ```
5. O servidor estará disponível em `http://127.0.0.1:5000`.

Para habilitar o debugger interativo, isso deve ser feito apenas localmente e de forma explícita:

```sh
set APP_ENV=development
set FLASK_DEBUG=true
python WebhookRediGlobal.py
```

Em produção, use um servidor WSGI e mantenha o debug desabilitado:

```sh
gunicorn --bind 0.0.0.0:%PORT% WebhookRediGlobal:app
```

O Flask não inicia o debugger quando `APP_ENV` não é `development`, mesmo que `FLASK_DEBUG` esteja definido.

## 🔧 Configuração

- A URL de destino base pode ser configurada na variável `BASE_TARGET_URL` no arquivo `WebhookRediGlobal.py`.
- Os logs são salvos no arquivo `webhook_logs.txt`.

## 📝 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.