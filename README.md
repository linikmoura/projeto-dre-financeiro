# 📊 Análise Financeira Automatizada com Python e MySQL

Projeto de automação de relatórios financeiros utilizando Python e MySQL, com geração automática de DRE, Fluxo de Caixa, análise por Centro de Custo e Margem de Lucro.

---

## 🎯 Objetivo

Automatizar o processo de análise financeira de uma empresa, eliminando a necessidade de planilhas manuais e gerando relatórios precisos e padronizados com poucos comandos.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Uso |
|---|---|---|
| Python | 3.11+ | Linguagem principal |
| MySQL | 8.0+ | Banco de dados |
| Pandas | 2.0+ | Manipulação de dados |
| PyMySQL | 1.1+ | Conexão Python ↔ MySQL |
| OpenPyXL | 3.1+ | Exportação para Excel |

---

## 📁 Estrutura do Projeto

```
projeto-dre-financeiro/
│
├── conexao_db.py              # Conexão com o banco de dados MySQL
├── etl.py                     # Extração e carga dos dados (CSV → MySQL)
├── dre.py                     # Geração da DRE mensal
├── fluxo_caixa.py             # Geração do Fluxo de Caixa anual
├── centrodecusto.py           # Análise de despesas por centro de custo
├── margemdelucro.py           # Análise de margem de lucro mensal
├── relatorio.py               # Exportação consolidada para Excel
└── lancamentos_financeiros.csv # Base de dados simulada (12 meses)
```

---

## ⚙️ Como Executar

### Pré-requisitos
- Python 3.11+
- MySQL 8.0+
- Bibliotecas: `pip install pymysql pandas openpyxl`

### Passo a passo

**1. Clone o repositório:**
```bash
git clone https://github.com/linikmoura/projeto-dre-financeiro.git
cd projeto-dre-financeiro
```

**2. Crie o banco de dados no MySQL:**
```sql
CREATE DATABASE IF NOT EXISTS financeiro;
USE financeiro;

CREATE TABLE IF NOT EXISTS lancamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_lancamento DATE NOT NULL,
    descricao VARCHAR(255),
    categoria VARCHAR(100),
    tipo VARCHAR(50),
    valor DECIMAL(15,2) NOT NULL,
    centro_custo VARCHAR(100),
    mes_referencia INT,
    ano_referencia INT
);
```

**3. Configure a conexão em `conexao_db.py`:**
```python
conn = pymysql.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="financeiro"
)
```

**4. Carregue os dados:**
```bash
python etl.py
```

**5. Execute as análises:**
```bash
python dre.py
python fluxo_caixa.py
python centrodecusto.py
python margemdelucro.py
```

**6. Exporte o relatório Excel:**
```bash
python relatorio.py
```

---

## 📈 Análises Disponíveis

### 1. DRE — Demonstração do Resultado do Exercício
Calcula automaticamente Receita Bruta, Deduções, CMV, Lucro Bruto e Lucro Líquido por mês.

```
==========================================
   DRE — 01/2025
==========================================
  Receita Bruta:         R$    117,000.00
  (-) Deduções:          R$     11,700.00
  (=) Receita Líquida:   R$    105,300.00
  (-) CMV:               R$     38,000.00
  (=) Lucro Bruto:       R$     67,300.00
  (-) Despesas Oper.:    R$     27,800.00
  (=) Lucro Líquido:     R$     39,500.00
==========================================
```

### 2. Fluxo de Caixa Anual
Mostra entradas, saídas, saldo mensal e saldo acumulado mês a mês.

### 3. Despesas por Centro de Custo
Tabela comparativa das despesas por setor (RH, Comercial, Administrativo, Estoque, Fiscal) com totais mensais e anuais.

### 4. Margem de Lucro com Alertas Automáticos
Calcula margem percentual por mês e emite alertas quando:
- ⚠️ Margem abaixo de 20%
- 🔴 Lucro caiu mais de 10% em relação ao mês anterior
- 🚨 Despesa maior que receita

---

## 📊 Resultados do Ano (2025 — dados simulados)

| Indicador | Valor |
|---|---|
| Total Receitas | R$ 1.687.000,00 |
| Total Despesas | R$ 1.095.460,00 |
| Lucro Líquido | R$ 591.540,00 |
| Margem Anual | 35,06% |

---

## 🧠 Conceitos Aplicados

- **ETL** (Extract, Transform, Load) — pipeline de dados do CSV ao banco
- **SQL** — queries com GROUP BY, SUM, filtros por período
- **Pandas** — pivot tables, cálculos financeiros, soma acumulada
- **Automação** — geração de relatórios Excel sem intervenção manual
- **Alertas inteligentes** — identificação automática de anomalias financeiras

---

## 👨‍💻 Autor

**Linik Moura**  
Analista Financeiro | Ciências Contábeis | Especialista em Dados Financeiros  
[![GitHub](https://img.shields.io/badge/GitHub-linikmoura-black?logo=github)](https://github.com/linikmoura)

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar e adaptar.
