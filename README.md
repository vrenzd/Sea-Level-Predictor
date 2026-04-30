# freeCodeCamp - Sea Level Predictor

Solução para o projeto "Sea Level Predictor" do freeCodeCamp.

## O que o projeto faz

O projeto lê a base `epa-sea-level.csv`, cria um gráfico de dispersão com os dados históricos de nível do mar e adiciona duas linhas de regressão linear:

1. Uma linha usando todos os dados de 1880 até 2013, projetando até 2050.
2. Uma linha usando somente os dados de 2000 em diante, também projetando até 2050.

O gráfico final é salvo como:

```bash
sea_level_plot.png
```

## Como executar

```bash
pip install -r requirements.txt
python main.py
```

## Arquivos

- `sea_level_predictor.py`: solução principal.
- `epa-sea-level.csv`: base oficial do projeto.
- `main.py`: executa o gráfico e os testes.
- `test_module.py`: testes básicos incluídos no pacote.
- `requirements.txt`: dependências.
