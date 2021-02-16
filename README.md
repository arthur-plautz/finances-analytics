# finances-analytics
Tracking and Analyzing Expenses throughout many banks

## setup

- create .env file:
    ```
    export AUTH_USER=<user_cpf>
    export AUTH_PASS=<app_password>
    export AUTH_PATH="credentials/cert.p12"
    ```
    *.env.example*

- sign in into nubank:
    ```
    pynubank
    ```

- set environment:
    ```bash
    virtualenv -p python3 venv
    source venv/bin/activate
    source .env
    ```

- set requirements:
    ```bash
    pip install -r requirements.txt
    ```
