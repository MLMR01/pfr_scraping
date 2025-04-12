def table_finder(tree):

    table_list = []
    table_loc = []


    for t in tree.xpath('//table'):          #t is the table element of this For loop
        table_id = t.get('id')
        table_list.append(table_id)
        table_loc.append('Body')

    for c in tree.xpath('//comment()'):     #c is the comment element of this For loop
        com_text = c.text.strip()
        if '<table' in com_text:
            com_tree = html.fromstring(com_text)
            com_table = com_tree.xpath("//table")
            for i,c_table in enumerate(com_table, start=1):
                c_table_id  = c_table.get('id')
                table_list.append(c_table_id)
                table_loc.append('Comment')
    
    tables_found = list(zip(table_list,table_loc))

    return tables_found
