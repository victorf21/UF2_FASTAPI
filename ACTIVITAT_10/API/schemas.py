def tematica_schema(tematica) -> dict:
    return {
        "option": str(tematica[0]), 
    }

def tematiques_schema(tematiques) -> list:
    return [tematica_schema(tematica) for tematica in tematiques]

def paraula_schema(paraula) -> dict:
    return {
        "option": str(paraula[0]),
    }
