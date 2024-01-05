Backdoor Simples - Instruções
Descrição:
Este conjunto de scripts permite a criação de um Reverse Shell em Python, utilizando um backdoor simples. O servidor (backdoor.py) é responsável por receber comandos e o cliente (clientbackdoor.py) os executa.

Passos para Utilização:

Download dos Scripts:

Baixe os seguintes scripts em seu computador:
backdoor.py (servidor)
clientbackdoor.py (cliente)
Configuração do Servidor (backdoor.py):

Abra o script em um editor de texto ou ambiente de desenvolvimento.
Edite as variáveis:
target_host: Insira o endereço IP do seu servidor.
target_port: Escolha uma porta para a comunicação.
Configuração do Cliente (clientbackdoor.py):

Abra o script em um editor de texto ou ambiente de desenvolvimento.
Edite as variáveis:
target_host: Insira o endereço IP do servidor configurado anteriormente.
target_port: Utilize a mesma porta escolhida no servidor.
Execução do Servidor:

No terminal, execute o seguinte comando:

python backdoor.py

O servidor estará aguardando por conexões.
Execução do Cliente:

No terminal, execute o seguinte comando:

python clientbackdoor.py

O cliente se conectará ao servidor.
Envio e Execução de Comandos:

No terminal do servidor (backdoor.py), insira comandos (por exemplo, ls para listar arquivos) e pressione Enter. Os comandos serão enviados para o cliente, e a saída será exibida no terminal do servidor.
Encerramento da Conexão:

Para encerrar a conexão, digite exit no terminal do servidor.
Lembre-se de utilizar esses scripts de maneira ética e legal, obtendo permissão antes de executá-los em ambientes controlados. O uso inadequado pode ter sérias consequências legais.
