# Dash Holoniq Components

The following components are available:

**Alert** The Alert component is hidden if it has no children. When children are injected the Alert 
component sets its style to become visible

<p align="center"><img src="docs/img/alert-example.png"></p>


**ButtonLink** Allows you to create a clickable link within a multi-page app in
the same way as `dcc.Link`. The standard `dcc.Button` attributes `n_clicks` and `n_clicks_timestamp` have been 
added to ButtonLink. These attributes can be used for notification that the `ButtonLink` has 
been clicked. `ButtonLink` can be enabled/disabled allowing conditional control of the link via a Dash callback

**Form** The `Form` components normal submit action can be inhibited. The form data, as it would be 
reported by the a submit action, is available in a Dash callback via the components `form_data` attribute.


**InputWithIcon** Adds a font awesome glyph and tooltip to the end of a standard input box

<p align="center"><img src="docs/img/input-with-icon-example.png"></p>

```
import dash_holoniq_components as dhc

app.layout = html.Div([
    dhc.InputWithIcon(type='name', id ='name', icon='fa fa-user', tooltip="Hi Big Joe")
])

```

**LayoutRouter** The children of LayoutRouter are each wrapped in a Div that is
is hidden/shown based on the current value of the LayoutRouter 'switch' attribute.

The advantage of `LayoutRouter` over the [standard](https://dash.plot.ly/urls) approach to 
dynamic layout is that **ALL** the applications layout is rendered, but hidden, when the
Dash application starts. `LayoutRouter` overcomes the problem with the `standard` approach 
were callbacks linked to dynamic content are difficult to realise.

**PageTitle** Sets the page title:

<p align="center"><img src="docs/img/page-title-example.png"></p>


```
import dash_html_components as html
import dash_holoniq_components as dhc

app.layout = html.Div([
    dhc.PageTitle(title='My Site - Summary'),
    html.H2('My Page')
])

```

**PasswordWithShow** Password input with a show/hide icon that can be clicked to reveal the password

<p align="center"><img src="docs/img/password-example.png"></p>

**Redirect**  Allows the window history/location to be set to a new value

## Usage Demo

The demo is a simple signin form and user profile that makes use of all the components. 

To signin enter a name and password. The password will be checked to see if it's at least 
eight characters. If it is a browser is redirected to the users profile page.

To run the Python demo

        python usage.py

Then open [http://localhost:8050](http://localhost:8050)
   


## Building

To build the component source you must have python and node installed on 
your computer.

Create and activate a clean python environment, then:

```
    pip install -r requirements.txt
    npm install

    npm run build:lib
    npm run build:py
    npm run build-dist

```

## Debugging the javascript component source

A simple javascript demo `src\demo\index.html` is used to allow the javascript react to
be debugged. To debug the component, breakpoints etc:

    npm run demo

Then, in VSCODE, select `Debug JS Demo` from the lunch options and press `F5` to launch the 
Chrome debug configuration. You can now add breakpoints and single step through the javascript
code in VSCODE.

The jest tests also support debugging, launch `3. Jest All` or `5. Jest Current File` in VSCODE

## Debugging the python demo `usage.py`

In VSCODE select `Debug usage.py` from the lunch options and press `F5` to launch the 
Flask/Dash development server.

Open [http://localhost:8050](http://localhost:8050)

Set breakpoints as required.

## Project

The project skeleton was initially created with the cookiecutter template:

        cookiecutter  https://github.com/plotly/dash-component-boilerplate.git

This worked well, but for some reason the component doc strings did not show up
in VSCODE intellisense. This is also a problem with the Dash HTML and CORE
component libraries. The [dash-bootstrap-components](https://github.com/facultyai/dash-bootstrap-components)
library plays well with VSCODE so the project now uses its build system.


**Folder layout**

```
dash_holoniq_components     : build results output folder (npm run build-dist)
demo                        : React/JS demo for debugging js (npm run demo)
examples                    : Standalone python examples of component usage
src                         : React.js source for components 
    components              : dash holoniq components js source
        __tests__           : jest tests and debugging (npm run test)
usage.py                    : Dash/Flask python demo entry point
utils                       : odds & sods to support usage.py
```

## Acknowledgment

A big thankyou to the [dash-bootstrap-components](https://github.com/facultyai/dash-bootstrap-components)
team. This projects layout and build system is a close copy of the one developed by them.
