from model.model import EstoqueModel
from view.view import EstoqueView
from control.controller import EstoqueController

if __name__ == "__main__":
    host = 'localhost'
    user = 'root'
    password = 'samuellucas'
    database = 'senaccentro'

    model = EstoqueModel(host, user, password, database)
    view = EstoqueView()
    controller = EstoqueController(model, view)

    while True:
        controller.executar()
