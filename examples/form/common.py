from dash import html
import dash_holoniq_components as dhc

def big_center(text, id=None):
    if id:
        return html.H2(text, id=id, className='display-3 text-center')
    else:
        return html.H2(text, className='display-3 text-center')


def form_container(title, fields, id=None):

    if id:
        form = dhc.Form(fields, id=id, preventDefault=True)
    else:
        form = dhc.Form(fields, preventDefault=True)

    return html.Div(
        [
            html.Div(
                [
                    html.Div(className="col-md-2"),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Br(),
                                            html.H4(title),
                                            html.Br(),
                                            form,
                                            html.Br(),
                                        ],
                                        className="card-body",
                                    )
                                ],
                                className="card",
                            )
                        ],
                        className="col-md-8",
                    ),
                    html.Div(className="col-md-2"),
                ],
                className="row",
            )
        ],
        className="container-fluid",
    )


