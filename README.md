Backdoor Simples - Instruções
Descrição
Este conjunto de scripts permite a criação de um Reverse Shell em Python, utilizando um backdoor simples. O servidor (backdoor.py) é responsável por receber comandos e o cliente (clientbackdoor.py) os executa.

Passos para Utilização
1. Download dos Scripts
Baixe os seguintes scripts em seu computador:

backdoor.py (servidor)
clientbackdoor.py (cliente)
2. Configuração do Servidor (backdoor.py)
Abra o script backdoor.py em um editor de texto ou ambiente de desenvolvimento.

Edite as seguintes variáveis:

target_host: Insira o endereço IP do seu servidor.
target_port: Escolha uma porta para a comunicação.
3. Configuração do Cliente (clientbackdoor.py)
Abra o script clientbackdoor.py em um editor de texto ou ambiente de desenvolvimento.

Edite as seguintes variáveis:

target_host: Insira o endereço IP do servidor configurado anteriormente.
target_port: Utilize a mesma porta escolhida no servidor.
4. Execução do Servidor

No terminal, execute o seguinte comando:

"python backdoor.py"

O servidor estará aguardando por conexões.

5. Execução do Cliente
No terminal, execute o seguinte comando:


"python clientbackdoor.py"


O cliente se conectará ao servidor.

6. Envio e Execução de Comandos
No terminal do servidor (backdoor.py), insira comandos (por exemplo, ls para listar arquivos) e pressione Enter. Os comandos serão enviados para o cliente, e a saída será exibida no terminal do servidor.


7. Encerramento da Conexão
Para encerrar a conexão, digite exit no terminal do servidor.


Lembre-se de utilizar esses scripts de maneira ética e legal, obtendo permissão antes de executá-los em ambientes controlados. O uso inadequado pode ter sérias consequências legais.
