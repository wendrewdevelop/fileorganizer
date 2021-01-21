# Validador e organizador de arquivos

## Fluxo ##

1. O Arquivo é submetido via formulário
2. O formato e o tamanho são avaliados
3. Os arquivos são organizados nas pastas
4. Os arquivos são avaliados em sandbox, para
averiguação de risco

## Preparando ambiente para uso da aplicação ## 

Exportando as variaveis de ambiente do flask
```sh
Unix Bash (Linux, Mac, etc.):
$ export FLASK_APP=hello
$ flask run

Windows CMD:
> set FLASK_APP=hello
> flask run

Windows PowerShell:
> $env:FLASK_APP = "hello"
> flask run
```

## TODO ##

- [x] Se a pasta **unprocessed_files** estiver vazia, retornar uma mensagem e pular a função;

- [ ] Criar sandbox para varredura do arquivo;

- [x] Criar tag para sempre que houver arquivos não processador o sistema realizar os procedimentos;