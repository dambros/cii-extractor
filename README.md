## Extrator de metadados Centro Integrado de Inteligência - PA
Repositório contendo scripts auxiliares para extração de metadados dos docs do CII - PA. 

Os scripts em questão possibilitam receber diretórios de entrada e irá gerar um xml para cada arquivo, respeitando o mesmo path do documento inicial.

Nenhum arquivo original é removido/alterado, e mesmo que seja alterado um diretório de indexação após a primeira execução, os xmls anteriormente gerados para aqueles documentos serão mantidos.

Caso não seja possível ler algum arquivo durante a execução, a informação do arquivo com problema é acrescidoa ao log em ```./res/extractor.log```
 
### Requisitos

* Python 3.6+
* [Textract](https://textract.readthedocs.io/en/stable/installation.html)


### Configs


No arquivo ```config.py``` é possível definir todas as infos necessárias para execução do script, sendo eles: 

| Valor        | Definição           |
| ------------- |:-------------:|
| ```DH_FOLDER_PATH```      | Caminho do diretório contendo os documentos de tipo DH |
| ```CIOP_FOLDER_PATH```     | Caminho do diretório contendo os documentos de tipo CIOP      |
| ```SUMMARY_PATH``` | Caminho onde serão salvos o resumo da execução do script. Caso vazio, não serão gerado resumos      |

