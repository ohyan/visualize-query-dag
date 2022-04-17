import regex


def extract_dependencies(query):
    # delete comment
    query = regex.sub(r'--.*\n|#.*\n|/\*([^*]|\*[^/])*\*/', '', query)

    # get CTEs
    cte_pattern = r'(?:with|,)\s*(\w+)\s+as\s*(?<rec>\((?:[^\(\)]+|(?&rec))*\))'
    ctes = regex.finditer(cte_pattern, query, regex.IGNORECASE)
    queries = {cte.group(1): cte.group(2) for cte in ctes}

    # get main query
    main_pattern = r'\)[;\s]*select' if any(queries) else r'select'
    start_main = regex.search(main_pattern, query, regex.IGNORECASE).span()[0] + 1
    queries['main'] = query[start_main:].strip()

    # find reference table or CTEs
    ref_pattern = r'(?:from|join)\s+([`.\-\w]+)'
    dependencies = dict()
    for name, script in queries.items():
        refs = regex.findall(ref_pattern, script, regex.IGNORECASE)
        dependencies[name] = [ref for ref in refs]
    return dependencies