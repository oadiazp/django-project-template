# {{ cookiecutter.project_name }}

## Setup CI

In the Gitlab CI:
- Disable the shared runners
- Register the our own runner

In the Gitlab CI define two variables:
- PRIV_SSH_KEY: The private SSH key that have access to the deployment server.
- KNOWN_HOST_KEY: The known host key: to get it ```shell ssh-keyscan <deployment_host>```