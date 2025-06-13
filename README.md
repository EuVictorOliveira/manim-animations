# Animações com Python Manim

Projeto pessoal com foco na criação de animações matemáticas e computacionais utilizando a biblioteca [Manim](https://docs.manim.community/), que permite gerar vídeos vetoriais de alta qualidade por meio de scripts em Python.

---

## Tecnologias utilizadas

- [Python 3.11](https://www.python.org/)
- [Manim Community Edition](https://docs.manim.community/)
- [FFmpeg](https://ffmpeg.org/) — para renderização de vídeos
- [LaTeX (opcional)](https://www.latex-project.org/) — para exibir fórmulas matemáticas
- [VSCode / PyCharm] — para edição dos scripts (opcional)

---

## Estrutura do repositório

```plaintext
manin-animations/
├── scenes/                  # Scripts com as cenas (cada animação é uma classe)
├── media/                   # Vídeos gerados (MP4, GIF)
└── README.md                # Documentação do repositório
```

---

## Execução

### 1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/manim-animations.git
cd animacoes-manim
```

### 2. Execute uma animação com o Manim:

```bash
manim -pql scenes/cena1_introducao.py CenaIntroducao
```

Parâmetros úteis:

- `-p`: exibe o vídeo automaticamente
- `-ql`: renderiza em baixa qualidade (preview)
- `-qh`: renderiza em alta qualidade (produção)

---

## Exemplos de cenas

Cada script dentro da pasta `scenes/` contém uma ou mais classes que representam animações específicas. Você pode renderizar qualquer uma delas com o Manim, informando o nome da classe.

Os vídeos gerados ficam salvos na pasta `outputs/`.

---

## Funcionalidades

* Criação de animações com Python
* Visualização de conceitos matemáticos e computacionais
* Modularização por arquivos e cenas
* Renderização automática de vídeos

---

## Objetivo

Este projeto tem como finalidade explorar o potencial do **Manim** na criação de visualizações matemáticas e computacionais. Serve também como portfólio de aprendizado em animações educacionais programadas.

---

## Exemplo de uso

Você pode executar:

```bash
manim -pql scenes/<nome_arquivo_python> <nome_função>
```

O vídeo será gerado automáticamente

---

##  Referências

- [Documentação do Manim](https://docs.manim.community/)
- [Canal 3Blue1Brown](https://www.youtube.com/c/3blue1brown)
- [Repositório oficial](https://github.com/ManimCommunity/manim)
