# 1. Introdução
### Objetivo do Documento:

Descrever os testes realizados no sistema ICTest, um protótipo de sistema de gerenciamento de casos de teste. O foco é realizar testes black box abrangentes para identificar possíveis falhas e garantir que as funcionalidades principais do sistema funcionem conforme o esperado.
### Escopo:
Este documento cobre testes funcionais, de usabilidade, e de segurança, realizados em ambiente Windows e Kali Linux.
### Ferramenta de Bug Tracking:
Os bugs identificados serão registrados em um repositório GitHub, usando a seção de issues para detalhar cada problema.

# 2. Metodologia
### Tipo de Testes:
Testes Black Box, sem acesso ao código-fonte.
## Ambiente de Teste:
### Segurança:
Kali Linux
### Testes Gerais:
Windows
### Critérios de Aceitação:
Não há critérios de aceitação bem definidos; os testes buscam identificar o maior número possível de falhas.
# 3. Casos de Teste
## 3.1 Testes Funcionais
### Cadastro de Usuário:
Entrada: Informações válidas para cadastro de usuário.
#### Resultado Esperado:
O sistema deve criar o usuário com sucesso e redirecionar para a tela de login.
### Login de Usuário:
#### Entrada:
Credenciais válidas e inválidas.
#### Resultado Esperado:
O sistema deve permitir o login com credenciais corretas e mostrar mensagens de erro adequadas para credenciais inválidas.
### Criação de Projeto:
#### Entrada:
Informações válidas para criação de um novo projeto.
#### Resultado Esperado:
O sistema deve criar o projeto e exibi-lo na lista de projetos do usuário.
### Criação de Caso de Teste:
#### Entrada:
Detalhes válidos para um novo caso de teste.
#### Resultado Esperado:
O caso de teste deve ser criado e exibido no board do projeto.
### Atualização de Caso de Teste:
#### Entrada:
Alteração de informações em um caso de teste existente.
#### Resultado Esperado:
O sistema deve atualizar o caso de teste com as novas informações.
### Adição de Membro ao Projeto:
#### Entrada:
E-mail de um usuário existente.
#### Resultado Esperado:
O usuário deve ser adicionado ao projeto e ter acesso às suas funcionalidades.
## 3.2 Testes de Usabilidade
### Navegação pelo Sistema:
#### Objetivo:
Verificar se o usuário consegue navegar intuitivamente entre as funcionalidades do sistema.
#### Método:
Seguir os passos de um usuário comum e observar a facilidade de navegação.
### Clareza das Mensagens de Erro:
#### Objetivo:
Avaliar se as mensagens de erro são claras e ajudam o usuário a corrigir o problema.
#### Método:
Induzir erros (como falha no login) e analisar as mensagens exibidas.
## 3.3 Testes de Segurança
### Testes de Injeção SQL:
#### Objetivo:
Testar se o sistema é vulnerável a injeções SQL durante o login ou cadastro.
#### Método:
Inserir caracteres de injeção SQL nos campos de entrada.
### Cross-Site Scripting (XSS):
#### Objetivo:
Verificar se o sistema permite a execução de scripts maliciosos através de entradas de usuário.
#### Método:
Tentar injetar scripts nos campos de entrada e observar o comportamento do sistema.
### Testes de Autenticação:
#### Objetivo:
Avaliar a robustez do sistema de autenticação contra ataques de força bruta.
#### Método:
Utilizar ferramentas de brute force para tentar comprometer contas.
## 4. Report de Bugs
### Registro no GitHub:
Detalhar cada bug encontrado, com os passos para reprodução, gravidade, e sugestões de correção.
## 5. Análise de Resultados
Resumo dos Bugs Encontrados: Análise da severidade, tipos de bugs, e áreas do sistema mais afetadas.
### Recomendações:
Sugestões para mitigação dos problemas identificados.
## 6. Conclusão
### Sumário:
Avaliação geral do sistema com base nos testes realizados.
### Próximos Passos:
Recomendações para os desenvolvedores e possíveis melhorias futuras.