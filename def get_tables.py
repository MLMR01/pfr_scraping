def get_tables(loc, tree, t_id):
    
    from lxml import etree, html
    import requests

    
    loc_1 = 'bd'
    loc_2 = 'cm'

    if loc == loc_1:
        table = tree.find(f'.//table[@id="{t_id}"]')
    elif loc == loc_2:  
        comments = tree.xpath('//comment()')  # Get all comments

        for comment in comments:
            comment_text = comment.text.strip()
            if '<table' in comment_text:  # Ensure the comment contains a table
                comment_text = comment_text.removeprefix('<!--').removesuffix('-->').strip()
                try:
                    clean_html = html.fromstring(comment_text)
                    table = clean_html.find(f'.//table[@id="{t_id}"]')
                    if table is not None:
                        break  # Stop once the table is found
                except Exception:
                    continue
        else:
            return None  # Return None if no table is found

    if table is not None:
        return etree.tostring(table, pretty_print=True, encoding='unicode')

    return None
