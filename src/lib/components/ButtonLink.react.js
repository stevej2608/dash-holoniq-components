/* global window:true */

import PropTypes from 'prop-types';

import React, {Component} from 'react';

/**
 * Modified version of dash-core-components Link
 * 
 * https://github.com/plotly/dash-core-components/blob/master/src/components/Link.react.js
 * 
 */

/*
 * event polyfill for IE
 * https://developer.mozilla.org/en-US/docs/Web/API/CustomEvent/CustomEvent
 */
function CustomEvent(event, params) {
    // eslint-disable-next-line no-param-reassign
    params = params || {
        bubbles: false,
        cancelable: false,
        // eslint-disable-next-line no-undefined
        detail: undefined,
    };
    const evt = document.createEvent('CustomEvent');
    evt.initCustomEvent(
        event,
        params.bubbles,
        params.cancelable,
        params.detail
    );
    return evt;
}
CustomEvent.prototype = window.Event.prototype;

/**
 * ButtonLink allows you to create a clickable link within a multi-page app in
 * the same way as dcc.Link. The standard dcc.Button attributes `n_clicks` 
 * and `n_clicks_timestamp` have been added to ButtonLink. These attributes
 * can be used for notification that the ButtonLink has been clicked
 */
export default class ButtonLink extends Component {
    constructor(props) {
        super(props);
        this.updateLocation = this.updateLocation.bind(this);
    }

    updateLocation(e) {
        // prevent anchor from updating location
        e.preventDefault();
        const {href, refresh} = this.props;
        if (refresh) {
            window.location.pathname = href;
        } else {
            window.history.pushState({}, '', href);
            window.dispatchEvent(new CustomEvent('onpushstate'));
        }
        // scroll back to top
        window.scrollTo(0, 0);

        const props = this.props
        props.setProps({
          n_clicks: props.n_clicks + 1,
          n_clicks_timestamp: Date.now()
      })

    }

    render() {
        const {style, disabled, id, loading_state} = this.props;
        let {className, href} = this.props;

        if (disabled) {
          className += " disabled" 
          href = null
        }

        /*
         * ideally, we would use cloneElement however
         * that doesn't work with dash's recursive
         * renderTree implementation for some reason
         */
        return (
            <a
                data-dash-is-loading={
                    (loading_state && loading_state.is_loading) || undefined
                }
                id={id}
                className={className}
                style={style}
                href={href}
                onClick={e => this.updateLocation(e)}
            >
                {this.props.children}
            </a>
        );
    }
}

ButtonLink.propTypes = {
    /**
     * The ID of this component, used to identify dash components
     * in callbacks. The ID needs to be unique across all of the
     * components in an app.
     */
    id: PropTypes.string,
    /**
     * The URL of a linked resource.
     */
    href: PropTypes.string,
    /**
     * Set true to disable the component
     */

    disabled: PropTypes.bool,
    /**
     * Controls whether or not the page will refresh when the link is clicked
     */
    refresh: PropTypes.bool,
    /**
     * Often used with CSS to style elements with common properties.
     */
    className: PropTypes.string,
    /**
     * Defines CSS styles which will override styles previously set.
     */
    style: PropTypes.object,
    /**
     * The children of this component
     */
    children: PropTypes.node,
    /**
     * An integer that represents the number of times
     * that this element has been clicked on.
     */
    'n_clicks': PropTypes.number,
    /**
     * An integer that represents the time (in ms since 1970)
     * at which n_clicks changed. This can be used to tell
     * which button was changed most recently.
     */
    'n_clicks_timestamp': PropTypes.number,
    /**
     * Object that holds the loading state object coming from dash-renderer
     */
    loading_state: PropTypes.shape({
        /**
         * Determines if the component is loading or not
         */
        is_loading: PropTypes.bool,
        /**
         * Holds which property is loading
         */
        prop_name: PropTypes.string,
        /**
         * Holds the name of the component that is loading
         */
        component_name: PropTypes.string,
    }),

    /**
     * Dash-assigned callback that should be called whenever any of the properties change
     */
    'setProps': PropTypes.func,

};

ButtonLink.defaultProps = {
    refresh: false,
    n_clicks: 0,
    n_clicks_timestamp: -1,
};
