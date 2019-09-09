import {Component} from 'react';
import PropTypes from 'prop-types';
/* global window:true */

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

let INDEX = 0;
let push_last = ''

/**
 * Allows the window history/location to be set to a new value
 */
export default class Redirect extends Component {
    constructor(props) {
        super(props);
        // console.log('%d: Redirect.Constructor ID=%s', INDEX++, props.id)
        this.updateLocation = this.updateLocation.bind(this);
    }


    updateLocation(props) {
        const {href, refresh, id} = props;

        // console.log('%d: Redirect.updateLocation ID=%s, href=%s, refresh=%s', INDEX++, id, href, refresh)

        if (href && (href !== window.location.pathname || refresh) ) {
            if (refresh) {
                // console.log('%d: Redirect.refresh ID=%s, href=%s', INDEX++, id, href)
                window.location.pathname = href;
            } else {
                if (push_last !== href) {
                    push_last = href
                    // console.log('%d: Redirect.pushState ID=%s, href=%s', INDEX++, id, href)
                    window.history.pushState({}, '', href);
                    window.dispatchEvent(new CustomEvent('onpushstate'));
                }
            }
            // scroll back to top
            window.scrollTo(0, 0);
        }
    }

    componentWillReceiveProps(nextProps) {
        // console.log('%d: Redirect.componentWillReceiveProps ID=%s %s', INDEX++, this.props.id, JSON.stringify(nextProps))
        this.updateLocation(nextProps);
    }

    render() {
        // console.log('render')
        return null;
    }
}

Redirect.propTypes = {
    /**
     * The ID of this component, used to identify dash components
     * in callbacks. The ID needs to be unique across all of the
     * components in an app.
     */
    id: PropTypes.string.isRequired,

    /** href in window.location - e.g., "/my/full/pathname?myargument=1#myhash" */
    href: PropTypes.string,

    /** Refresh the page when the location is updated? */
    refresh: PropTypes.bool,

    /**
     * Dash-assigned callback that gets fired when the value changes.
     */
    setProps: PropTypes.func,
};

Redirect.defaultProps = {
    refresh: true,
};
