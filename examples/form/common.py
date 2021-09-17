from dash import html

def big_center(text, id=None):
    if id:
        return html.H2(text, id=id, className='display-3 text-center')
    else:
        return html.H2(text, className='display-3 text-center')
