FROM python:3.12.2-slim-bookworm

# Adiciona pacotes necessários para compilar dependências Python
RUN apt-get update && apt-get install -y libpq-dev build-essential

# Define o diretório de trabalho dentro do contêiner
WORKDIR /src

# Copia apenas o arquivo de requisitos primeiro
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código-fonte da aplicação para o diretório de trabalho
COPY . .

# Define a porta em que a aplicação irá escutar
EXPOSE 8000

# Cria as tabelas no banco de dados e inicia o servidor
CMD ["sh", "-c", "python src/config/database.py && uvicorn app:app --host 0.0.0.0 --port 8000"]
