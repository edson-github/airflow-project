# Projeto de Aprendizado em Engenharia de Dados com Airflow

Este projeto é um ambiente de aprendizado para engenharia de dados utilizando o Apache Airflow. O objetivo é fornecer uma estrutura básica para entender os conceitos fundamentais de orquestração de pipelines de dados.

## 🚀 Visão Geral

O projeto demonstra como:
- Configurar um ambiente local do Airflow com Docker Compose
- Criar DAGs (Directed Acyclic Graphs) para orquestração de tarefas
- Implementar operadores básicos do Airflow
- Gerenciar dependências entre tarefas
- Monitorar execuções de pipelines

## 📋 Pré-requisitos

- Python 3.8+
- Docker e Docker Compose
- Git

## ⚠️ Notas Importantes Antes de Rodar

1. **Inicialização do Banco de Dados do Airflow**

   Antes de iniciar os containers, é necessário rodar o comando abaixo para inicializar o banco de dados do Airflow:

   ```bash
   docker compose run --rm webserver airflow db migrate
   ```

2. **Chave Fernet**

   Certifique-se de que a variável `AIRFLOW__CORE__FERNET_KEY` está definida corretamente no `.env` ou no `docker-compose.yml`, com uma chave válida de 32 bytes codificada em base64. Você pode gerar uma chave com o seguinte comando Python:

   ```python
   from cryptography.fernet import Fernet
   print(Fernet.generate_key().decode())
   ```

3. **Criação de Usuário Admin**

   Após a inicialização do banco, crie um usuário para acesso à interface web:

   ```bash
   docker compose run --rm webserver airflow users create \
     --username admin \
     --firstname Admin \
     --lastname User \
     --role Admin \
     --email admin@example.com \
     --password admin
   ```

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd airflow-project
```

2. Inicie o ambiente Airflow usando Docker Compose:
```bash
docker compose up -d
```

3. Acesse a interface web do Airflow:
```
http://localhost:8080
```
- Usuário: admin
- Senha: admin

## 📁 Estrutura do Projeto

```
airflow-project/
├── dags/                    # Diretório para suas DAGs
├── plugins/                 # Plugins personalizados
├── data/                    # Dados de exemplo
├── docker-compose.yml       # Configuração do Docker
├── .env                     # Variáveis de ambiente, incluindo a Fernet Key
└── README.md                # Este arquivo
```

## 📚 Exemplos Incluídos

O projeto inclui exemplos de DAGs para:
- Extração de dados de APIs
- Transformação de dados
- Carregamento em banco de dados
- Agendamento de tarefas
- Tratamento de erros

## 🎯 Objetivos de Aprendizado

- Entender os conceitos básicos do Airflow
- Aprender a criar e gerenciar DAGs
- Compreender a execução de tarefas em paralelo
- Implementar boas práticas de engenharia de dados
- Monitorar e depurar pipelines

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Adicionar novos exemplos
- Compartilhar conhecimento

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Suporte

Para dúvidas ou sugestões, abra uma issue no repositório.
```

---

Se quiser, posso te ajudar a atualizar o arquivo no repositório diretamente (via terminal ou GitHub). Deseja que eu também atualize o `.env.example` com a variável `FERNET_KEY` e outras sugestões.