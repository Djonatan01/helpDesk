# helpDesk
 Sistema de helpdesk Governaça de TI Charles

#### Configuração do Projeto
* Primeiro, crie um ambiente virtual para hospedar as dependências do projeto.
Instale as dependências necessárias com os seguintes comandos:

#### Linux:

```bash
cd ~/Documentos  # Navega até o diretório "Documents"

python3 -m venv .venv  # Cria um ambiente virtual chamado ".venv"
source .venv/bin/activate  # Ativa o ambiente virtual

pip install -r requirements.txt  # Instala as dependências listadas no arquivo "requirements.txt"
```

#### Windows:

```bash
cd C:\Users\SeuUsuario\Documentos  # Navega até o diretório "Documents"

python -m venv .venv  # Cria um ambiente virtual chamado ".venv"
.venv\Scripts\activate  # Ativa o ambiente virtual

pip install -r requirements.txt  # Instala as dependências listadas no arquivo "requirements.txt"

```

#### Então, inicialize o servidor da API:

```bash
python main.py
```
