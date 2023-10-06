import pymongo

client_conn = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.k45yjfv.mongodb.net/?retryWrites=true&w=majority")

pacientes_col = client_conn.db_clinica.pacientes


filter_ = {
    "idade": {"$gte": 30}
}

projection_ = { # select, onde estiver 1 = seleciona e 0 = não seleciona
    "_id": 0,
    "nome_paciente": 1,
    "idade": 1
}

res = list(pacientes_col.find(filter_, projection_))

print(res)


