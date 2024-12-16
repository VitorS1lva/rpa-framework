# ***TODO***
> organizar as utilities
> refatorar o código de get_queue_items_from_db.py (para comportar limite de 1 item no retorno da query)
> criar lógica de leitura e criação de job no orquestrador
> criar tool de criação de queue items

# ***TODO para final do processo***  
> estudar integração do processo com o data dog
> estudar integração do processo com o secret vault
> criar fluxograma de integração de aplicações conforme solicitado pela Nathanaelly https://app.creatly.com/d/gCrTdryjGQ6/edit
> finalizar fluxograma do projeto
> criar documentações para o projeto, para cada módulo
> criar UML do projeto
> #IMPORTANTE = Definir integração com as atividades moduladas e seu armazenamento
> revisar a estrutura dos queue itens, adicionar mais colunas com mais informações, data de execução, etc...
> criar lógica de captura de erro durante o framework e atualização de status do JOB (SE ou Sucess), importante lembrar que é mais interessante que o registro do job seja criado no final da execução, talvez no final state, lembrar TAMBÉM que o framework precisa consultar o snowflake para pegar o último id do job executado, acrescentar um ao seu valor e assim gerar um novo ID