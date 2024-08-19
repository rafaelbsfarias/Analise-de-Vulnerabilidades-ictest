# 3.1 Testes funcionais

### Cadastro de Usuário:

O campo `nome` permite cadastro de strings formadas apenas por caracteres especiais.

O campo `nome` permite cadastro de strings formadas apenas por números.

O cadastro não garante o uso de um e-mail válido

O cadastro não força a escolha de senhas fortes. (123456 e 123qwe são senhas aceitas no cadastro)

Aviso de cadastro realizado com sucesso funciona da forma esperada.

Comportamento de redirecionamento para tela de login, após cadastro, efetuada com sucesso. 

#### inputs testados:

```
nome:   rafael
e-mail: rafael.serejo@ufba.br
senha:  123qwe

nome:   Teste
e-mail: teste@email-invalido.com
senha:  123456

nome:   123
e-mail: 123@123.com
senha:  123qwe

nome:   !@#
e-mail: qwe@qwe.com
senha:  123456
```


### Login de Usuário:

Teste de credenciais válidas e inválidas realizadas, o sistema se comporta como esperado.

Em caso de credenciais válidas o login é efetuado
Em cado de credenciais invalidas a mensagem `Email/senha incorreto, tente novamente!` é exibida

Autenticação com comportamento esperado, contudo ao utilizar o Burp Suite como proxy podemos interceptar uma resposta interessante. 

![REQUEST](BurpSuit/Captura-apos-login.png)
![REQUEST](BurpSuit/Captura-apos-login2.png)

Conforme as imagens acima podemos ver que ao solicitar o GET da pagina projects recebos em .jason a lista de todos os usuários com o `hash_password` de cada um deles.

### Criação de Projeto:
A criação de projetos ocorre perfeitamente, contudo, não existe caminho para deletar um projeto e não é possivel visualizar a descrição do projeto e é possivel a criação de projetos duplicados.

#### inputs testados:

```
nome:           Procurando bugs
descrição:      Projeto para procurar bugs
código:         RBSF0001

nome:           Descrição
descrição:      Não consigo visualizar a descrição do projeto após a criação.
código:         RBSF0002

nome:           Descrição
descrição:      Não consigo visualizar a descrição do projeto após a criação.
código:         RBSF0002

```
![criação-projeto](Criação-Projeto.png)
![Projeto-Duplicado](Projeto-Duplicado.png)

### Criação de Caso de Teste:
Casos de teste são criados perfeitamente, fácil e intuitivamente

#### inputs testados:

```
Título: Cadastro com e-mail inválido 
Descrição: Foi testado na se a plataforma aceitaria um email inválido 
Tipo de teste: Funcional
Responsável: Teste01
Prazo: 2024-08-15
Prioridade: Média
Anexos: ![caso-teste](caso-teste.jpg)
```

### Atualização de Caso de Teste:

As atualizações funcionam perfeitamente

Testes realizados: alterar status do caso de teste, modificar o conteúdo do caso de teste.

### Adição/exclusão de Membro ao Projeto:

Ações funcionando perfeitamente

## 3.2 Testes de Usabilidade
### Navegação pelo Sistema:
Um usuário consegue apagar casos de teste de outro projeto, no qual, ele não faz parte.

login > Projetos, seleciona qualquer projeto na lista > clica em qualquer caso de teste do projeto > no canto superior esquerdo clica no simbolo de lixeira.

Não foi localizado uma forma de excluir um projeto.

Demais funcionalidades são bem intuitivas e de fácil uso.

### Clareza das Mensagens de Erro:

são claras e ajudam o usuário a corrigir o problema.

## 3.3 Testes de Segurança
### Testes de Injeção SQL:
Aparenta ser um nível de proteção aceitavel contra SQLi, para o teste foi utilizado o sqlmap 1.8.2#stable

### Cross-Site Scripting (XSS):
Cabeçalho de Política de Segurança de Conteúdo (CSP) Não Configurado:

Descrição: O site não configurou a Política de Segurança de Conteúdo (CSP), o que pode permitir a injeção de conteúdo malicioso.

Solução: Configure o cabeçalho CSP para mitigar o risco de XSS e outros ataques de injeção de conteúdo.



### Cabeçalhos de Segurança Ausentes:

Timestamp Disclosure - Unix: O servidor revelou informações sensíveis sobre o tempo do sistema operacional.
X-Content-Type-Options Header Missing: O cabeçalho X-Content-Type-Options, que ajuda a prevenir ataques de MIME sniffing, está ausente.
Anti-Clickjacking Header Ausente: Falta o cabeçalho para proteger contra ataques de clickjacking.