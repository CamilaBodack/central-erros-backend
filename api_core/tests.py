from django.test import TestCase

# Create your tests here.

""" Estrutura:
1. Usuário deve ter um registro válido.
2. Validação do usuário via token.
3. Se usuário + token forem válidos usuário deve ter acesso.
- Libs de autenticação, form
  (https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Authentication)
    Endpoints:
1. Estrutura que recebe os erros dos locais: backend, frontend,
via mobile, via desktop
2. Filtar os erros por fonte
3. Endpoint para expor os dados solicitados,
   informação deve ser enviada no formato de log.
"""