# 📁 Python File Organizer

> Um script de automação leve e robusto projetado para limpar diretórios caóticos, organizando automaticamente arquivos em pastas categorizadas, com tratamento de erros integrado e geração de relatórios de execução.

---

## 🚀 Funcionalidades

- **Categorização Automática:** Organiza arquivos em pastas específicas (`Imagens`, `Documentos`, `Videos`, `Compactados`, `Instaladores`, etc.) com base em suas extensões.
- **Proteção contra Duplicados:** Evita sobrescrever arquivos verificando se já existe um arquivo com o mesmo nome na pasta de destino.
- **Tratamento de Erros:** Blocos `try-except` robustos para capturar erros de permissão (arquivos abertos em outros programas) e exceções inesperadas sem interromper a execução.
- **Relatório de Execução (Log):** Gera um relatório em texto detalhado (`relatorio_organizacao.txt`) ao final de cada execução, contendo data, hora, ações tomadas e um resumo de sucessos, arquivos ignorados e erros.
- **Sem Dependências Externas:** Desenvolvido inteiramente com a biblioteca padrão do Python (`pathlib`, `shutil`, `datetime`), sem necessidade de instalações complexas.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- `pathlib` (Manipulação moderna de caminhos)
- `shutil` (Operações de alto nível em arquivos)
- `datetime` (Geração de carimbo de data/hora para os logs)

---

## 📦 Como Usar

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/organizador-de-arquivos.git](https://github.com/SEU-USUARIO/organizador-de-arquivos.git)
   cd organizador-de-arquivos

2. **Configure o caminho de destino:**

Abra o arquivo main.py e altere a variável pasta_para_organizar para o diretório que você deseja organizar.

3. **Execute o script:**

```bash
    python main.py
```
4. **Verifique os resultados:**

-Abra o diretório escolhido para ver suas pastas organizadas e o arquivo de log relatorio_organizacao.txt gerado.


# Estrutura do Projeto

organizador-de-arquivos/
│
├── main.py                    # Script principal de automação e lógica
├── relatorio_organizacao.txt  # Relatório de log gerado após a execução
└── README.md                  # Documentação do projeto


# 🤝 Contribuindo

Contribuições, issues e solicitações de recursos são sempre bem-vindos! Sinta-se à vontade para verificar a aba de [suspicious link removed].