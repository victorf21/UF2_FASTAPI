def theme_schema(tematica) -> dict:
    return {
        "option": str(tematica[0]),           
    }

def themes_schema(tematiques) -> list:
    return [theme_schema(tematica) for tematica in tematiques]

