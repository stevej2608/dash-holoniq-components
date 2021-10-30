import json
import dash
from dash import html
from utils import logging
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

from app import app
from .common import form_container

NOUPDATE = dash.no_update

def formFields():

    # https://dash-bootstrap-components.opensource.faculty.ai/docs/components/input/

    radioitems = html.Div([
            dbc.Label("Radio Item - choose one"),
            dbc.RadioItems(name="radio-item",
                options=[
                    {"label": "Option 1", "value": 1, "input_id": "rad1"},
                    {"label": "Option 2", "value": 2, "input_id": "rad2"},
                    {"label": "Disabled Option", "value": 3, "disabled": True},
                ],
                value=1,
            ),
        ], className='mb-3')

    checklist = html.Div([
            dbc.Label("Checklist - choose a bunch"),
            dbc.Checklist(
                options=[
                    {"label": "Option 1", "value": 1, "input_id": "chk1"},
                    {"label": "Option 2", "value": 2, "input_id": "chk2"},
                    {"label": "Disabled Option", "value": 3, "input_id": "opt3", "disabled": True},
                ],
                value=[1],
            )
        ], className='mb-3')

    switches = html.Div([
            dbc.Label("Checklist - toggle a bunch"),
            dbc.Checklist(
                options=[
                    {"label": "Option 1", "value": 1, "input_id": "tog1"},
                    {"label": "Option 2", "value": 2, "input_id": "tog2"},
                    {"label": "Disabled Option", "value": 3,"input_id": "toggle3", "disabled": True},
                ],
                value=[1],
                switch=True,
            )
        ], className='mb-3')

    button = html.Div(
        html.Button("Submit", id="form_submit", type="submit", disabled=False, className="btn btn-primary btn-block"),
        className="form-group m-0",
    )

    return [radioitems, checklist, switches, button]


def layout():

    @app.callback(Output("report", "children"),Input("checkbox-form", "form_data"))
    def _callback(form_data):
        report = NOUPDATE

        if form_data:
            del form_data['submit_count']
            values = {'form_data': form_data}
            report = json.dumps(values, sort_keys=True, indent=2)

        return report

    form = form_container("Check box examples", formFields(), id="checkbox-form")
    return html.Div([form, html.H4(id='report')
    ])

#
# python -m examples.form.checkbox_form
#
# http://localhost:8060
#

if __name__ == "__main__":
    print("\nvisit: http://localhost:8060\n")

    aps_log = logging.getLogger("werkzeug")
    aps_log.setLevel(logging.ERROR)

    app.layout = layout()
    app.run_server(host='0.0.0.0', port=8060, debug=False, threaded=False)
