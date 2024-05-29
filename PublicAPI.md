**Sistema de Gestion de Tareas**

API

Todos los metodos son publicos, por lo tanto no es necesiario una autenticacion para realizar las operaciones.

Metodos permitidos `GET, POST, PUT, DELETE`

Listar todas las tareas

    GET /tasks/api/tasks/

ejemplo curl: 

    curl --request GET \
      --url {host}/tasks/api/tasks/

Crear una tarea
parametros obligatorios: `title, email, description`

    POST /tasks/api/tasks/
    
ejemplo curl:

    curl --request POST \
      --url {host}/tasks/api/tasks/ \
      --header 'Content-Type: application/json'
      --data '{
    	"title": "title",
    	"email": "example@example.com",
    	"description": "description"
    }'

Actualizar una tarea

    PUT /task/api/tasks/{id}

ejemplo curl:

       curl --request PUT \
      --url http://127.0.0.1:8000/tasks/api/tasks/9/ \
      --header 'Content-Type: application/json'\
      --data '{
        "id": 9,
        "title": "title",
        "description": "description",
        "email": "email@email.com"
    }'

Eliminar una tarea

    DELETE /task/api/tasks/{id}


ejemplo curl:

     curl --request DELETE \
      --url http://127.0.0.1:8000/tasks/api/tasks/3/ \
      --header 'Content-Type: application/json'
