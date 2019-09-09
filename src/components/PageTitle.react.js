/* global window:true */

import PropTypes from 'prop-types';
import { Component } from 'react';

// https://stackoverflow.com/questions/40044411/override-document-title-then-use-original-method

Object.defineProperty(document, 'title', {
    set: function (newValue) {
        if(newValue !== "Updating..." && newValue !== "Dash"){
            document.getElementsByTagName("title")[0].innerHTML = newValue;
        }
    },

    get: function () {
        return document.getElementsByTagName("title")[0].innerHTML;
    }
});

/**
 * Sets the page title
 */

export default class PageTitle extends Component {

    constructor(props) {
        super(props);
    }


    componentWillReceiveProps(nextProps) {
        const {title} = nextProps;
        if (title) {
            console.log('Title %s', title)
            document.title = title;
        }
    }    

    render() {

        const {title} = this.props;
        if (title) {
            console.log('Title %s', title)
            document.title = title;
        }

        return null
    }
}

PageTitle.propTypes = {
    /**
     * The ID of this component, used to identify dash components
     * in callbacks. The ID needs to be unique across all of the
     * components in an app.
     */
    id: PropTypes.string,
    /**
     * The the page title.
     */
    title: PropTypes.string,
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
};

PageTitle.defaultProps = {

};
