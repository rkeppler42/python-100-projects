# 01 — Rename Filenames

> 🇧🇷 [Português](#português) | 🇺🇸 [English](#english)

---

## English

### About

A Python script that batch-renames all files in a directory by appending the current date (in `YYYY-MM-DD` format) to each filename.

**Example:**

```
a.txt  →  a-2024-08-16.txt
b.txt  →  b-2024-08-16.txt
```

### How to Run

1. Place the files you want to rename inside a folder named `files` in the same directory as `main.py`
2. Run the script:

```bash
python main.py
```

3. The terminal will confirm each rename:

```
Renamed 'a.txt' to 'a-2024-08-16.txt'
Renamed 'b.txt' to 'b-2024-08-16.txt'
...
File renaming completed.
```

### Libraries Used

| Library | Purpose | Installation |
|---------|---------|--------------|
| `os` | Iterate and rename files | Standard library |
| `datetime` | Get current date | Standard library |

---

## Português

### Sobre

Um script Python que renomeia em lote todos os arquivos de um diretório, adicionando a data atual (no formato `YYYY-MM-DD`) ao nome de cada arquivo.

**Exemplo:**

```
a.txt  →  a-2024-08-16.txt
b.txt  →  b-2024-08-16.txt
```

### Como Executar

1. Coloque os arquivos que deseja renomear dentro de uma pasta chamada `files`, no mesmo diretório que `main.py`
2. Execute o script:

```bash
python main.py
```

3. O terminal confirmará cada renomeação:

```
Renamed 'a.txt' to 'a-2024-08-16.txt'
Renamed 'b.txt' to 'b-2024-08-16.txt'
...
File renaming completed.
```

### Bibliotecas Utilizadas

| Biblioteca | Uso | Instalação |
|------------|-----|------------|
| `os` | Iterar e renomear arquivos | Biblioteca padrão |
| `datetime` | Obter a data atual | Biblioteca padrão |