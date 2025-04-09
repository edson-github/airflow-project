# Projeto de Aprendizado em Engenharia de Dados com Airflow

Este projeto é um ambiente de aprendizado para engenharia de dados utilizando o Apache Airflow. O objetivo é fornecer uma estrutura básica para entender os conceitos fundamentais de orquestração de pipelines de dados.

## 🚀 Visão Geral

O projeto demonstra como:
- Configurar um ambiente local do Airflow
- Criar DAGs (Directed Acyclic Graphs) para orquestração de tarefas
- Implementar operadores básicos do Airflow
- Gerenciar dependências entre tarefas
- Monitorar execuções de pipelines

## 📋 Pré-requisitos

- Python 3.8+
- Docker e Docker Compose
- Git

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd airflow-project
```

2. Inicie o ambiente Airflow usando Docker Compose:
```bash
docker-compose up -d
```

3. Acesse a interface web do Airflow:
```
http://localhost:8080
```
- Usuário: airflow
- Senha: airflow

## 📁 Estrutura do Projeto

```
airflow-project/
├── dags/                    # Diretório para suas DAGs
├── plugins/                 # Plugins personalizados
├── data/                    # Dados de exemplo
├── docker-compose.yml       # Configuração do Docker
└── README.md               # Este arquivo
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
