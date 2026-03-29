<div align="center">

# ✉ MailMul

**Email alias generator via command line**

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

🌐 **Language / Idioma:** [🇺🇸 English](#-english) · [🇧🇷 Português](#-português)

</div>

---

## 🇺🇸 English

### 📌 What is it?

MailMul generates multiple valid aliases from a single email address using two well-known techniques supported by most email providers (Gmail, etc.):

| Technique | Example | Behavior |
|-----------|---------|----------|
| **Dot-trick** | `u.ser@gmail.com` | Delivered to the same inbox |
| **Plus-trick** | `user+shop@gmail.com` | Delivered to the same inbox |

This is useful for testing sign-up flows, filtering emails, or any scenario where you need multiple addresses pointing to the same inbox.

### ⚡ Installation

No external dependencies — just Python 3.10+.

```bash
git clone https://github.com/mrofcodyx/MailMul.git
cd MailMul
python3 mailmul.py
```

### 🚀 Usage

**Interactive mode** — just run without arguments and follow the prompts:
```bash
python3 mailmul.py
```

**CLI mode:**
```bash
python3 mailmul.py -e user@gmail.com -n 20          # generate 20 aliases
python3 mailmul.py -e user@gmail.com -n 50 -s       # generate and save to file
python3 mailmul.py -e user@gmail.com -n 30 -q       # quiet mode (pipe-friendly)
python3 mailmul.py -e user@gmail.com -n 100 -q -s   # quiet + save
python3 mailmul.py -h                                # show help
```

**Available flags:**

| Flag | Long form | Description |
|------|-----------|-------------|
| `-e` | `--email`  | Target email address |
| `-n` | `--number` | Number of aliases to generate (default: 10) |
| `-s` | `--save`   | Save output to `output/<name>.lst` |
| `-q` | `--quiet`  | Suppress banner — ideal for piping |
| `-h` | `--help`   | Show help message |

### ⚙️ How it works

MailMul combines two alias strategies:

- **Dot-trick** — inserts dots between characters in the username. Gmail (and others) ignores dots, so `u.s.e.r@gmail.com` and `user@gmail.com` are the same inbox. The number of possible variants grows exponentially with username length.
- **Plus-trick** — appends a `+tag` suffix to the username. Everything after `+` is ignored by the mail server, but you can use it for filtering rules.

When you request more aliases than dot-trick variants can provide, the generator fills the remaining slots with plus-trick aliases automatically.

### � Output

When using `-s`, aliases are saved to:
```
output/<username>.lst
```

One alias per line, ready to pipe into other tools.

---

<br>

---

## 🇧🇷 Português

### 📌 O que é?

MailMul gera múltiplos aliases válidos a partir de um único endereço de email, usando duas técnicas amplamente suportadas por provedores como Gmail:

| Técnica | Exemplo | Comportamento |
|---------|---------|---------------|
| **Dot-trick** | `u.ser@gmail.com` | Chega na mesma caixa de entrada |
| **Plus-trick** | `user+loja@gmail.com` | Chega na mesma caixa de entrada |

Útil para testar fluxos de cadastro, criar filtros de email ou qualquer situação onde você precisa de múltiplos endereços apontando para a mesma caixa.

### ⚡ Instalação

Sem dependências externas — apenas Python 3.10+.

```bash
git clone https://github.com/mrofcodyx/MailMul.git
cd MailMul
python3 mailmul.py
```

### 🚀 Uso

**Modo interativo** — execute sem argumentos e siga as instruções:
```bash
python3 mailmul.py
```

**Modo CLI:**
```bash
python3 mailmul.py -e user@gmail.com -n 20          # gerar 20 aliases
python3 mailmul.py -e user@gmail.com -n 50 -s       # gerar e salvar em arquivo
python3 mailmul.py -e user@gmail.com -n 30 -q       # modo silencioso (pipe)
python3 mailmul.py -e user@gmail.com -n 100 -q -s   # silencioso + salvar
python3 mailmul.py -h                                # exibir ajuda
```

**Flags disponíveis:**

| Flag | Forma longa | Descrição |
|------|-------------|-----------|
| `-e` | `--email`   | Email alvo |
| `-n` | `--number`  | Quantidade de aliases (padrão: 10) |
| `-s` | `--save`    | Salvar em `output/<nome>.lst` |
| `-q` | `--quiet`   | Sem banner — ideal para pipe |
| `-h` | `--help`    | Exibir ajuda |

### ⚙️ Como funciona

MailMul combina duas estratégias de alias:

- **Dot-trick** — insere pontos entre os caracteres do nome de usuário. O Gmail (e outros) ignora pontos, então `u.s.e.r@gmail.com` e `user@gmail.com` são a mesma caixa. O número de variantes possíveis cresce exponencialmente com o tamanho do nome.
- **Plus-trick** — adiciona um sufixo `+tag` ao nome de usuário. Tudo após o `+` é ignorado pelo servidor de email, mas pode ser usado para criar regras de filtro.

Quando você solicita mais aliases do que o dot-trick consegue gerar, o restante é preenchido automaticamente com aliases do plus-trick.

### 📁 Saída

Ao usar `-s`, os aliases são salvos em:
```
output/<usuario>.lst
```

Um alias por linha, pronto para ser usado com outras ferramentas via pipe.

---

<div align="center">

## 👤 Autor / Author

Developed by **Mr_ofcodyx**

<sub>MailMul v2.0.0 — MIT License</sub>

</div>
