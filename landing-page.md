# dash-holoniq-components

A set of house-keeping components for [Dash][dash-homepage] that make the
implementation of forms and larger, multi-page applications a little easier.

The following components are available:

**Alert** The Alert component is hidden if it has no children. When children are injected the Alert
component sets its style to become visible

**ButtonLink** Allows you to create a clickable link within a multi-page app in
the same way as `dcc.Link`. The standard `dcc.Button` attributes `n_clicks` and `n_clicks_timestamp` have been
added to ButtonLink. These attributes can be used for notification that the `ButtonLink` has
been clicked. `ButtonLink` can be enabled/disabled allowing conditional control of the link via a Dash callback

**Form** The `Form` components normal submit action can be inhibited. The form data, as it would be
reported by the a submit action, is available in a Dash callback via the components `form_data` attribute.

**InputWithIcon** Adds a font awesome glyph and tooltip to the end of a standard input box

**LayoutRouter** The children of LayoutRouter are each wrapped in a Div that is
is hidden/shown based on the current value of the LayoutRouter 'switch' attribute.

The advantage of `LayoutRouter` over the [standard](https://dash.plot.ly/urls) approach to
dynamic layout is that **ALL** the applications layout is rendered, but hidden, when the
Dash application starts. `LayoutRouter` overcomes the problem with the `standard` approach
were callbacks linked to dynamic content are difficult to realise.

**PageTitle** Sets the page title:

**PasswordWithShow** Password input with a show/hide icon that can be clicked to reveal the password

**Location** A modified version of *dash-core-components* Location component. Allows multiple instances
to co-exist. In the *dash-core-components* version the last instance is the only one
to get history event notifications.

**Button**

A modified version of *dash-core-components* Button component. The component
has a boolean *focus* attribute that is set true when the button gains
focus and false when it looses it. The focus attribute can be used in a dash
callback to hide an associated dropdown whenever the user clicks
the application background or makes a selection from the dropdown.

*Example dropdown callback*
```
    @callback(Output(ids.container(MATCH), 'className'),
            Input(ids.button(MATCH), 'n_clicks'),
            Input(ids.button(MATCH), 'focus'),
            State(ids.container(MATCH), 'className'))
    def show_dropdown(button_clicks, button_focus, className):
        logging.info('show_dropdown: button_clicks=%s, className = %s', button_clicks, className)

        if not button_clicks:
            return className

        if 'show' in className and button_focus == False:
            return className.replace(' show', '')
        else:
            return className + ' show'
```
## Installation

### PyPI

You can install *dash-holoniq-components* with `pip`:

```
pip install dash-holoniq-components
```

## Documentation

Head over to the [*README*][docs-homepage] for more details.

## Contributing

The source code for *dash-bootstrap-components* is available
[on GitHub][dhc-repo]. If you find a bug or something is unclear, we encourage
you to raise an issue. We also welcome contributions, to contribute, fork the
repository and open a [pull request][dhc-pulls].


[dash-homepage]: https://dash.plot.ly/
[dhc-repo]: https://github.com/stevej2608/dash-holoniq-components
[docs-homepage]: https://github.com/stevej2608/dash-holoniq-components/blob/master/README.md
[dhc-pulls]: https://github.com/stevej2608/dash-holoniq-components/pulls
