import React, { Component } from 'react';
import PropTypes from 'prop-types';

/**
 * The children of LayoutRouter are each wrapped in a Div that is
 * is hidden/shown based on the current value of the LayoutRouter 'switch' 
 * attribute.
 */

export default class LayoutRouter extends Component {

  constructor(props) {
    super(props);
  }


  render() {
    const props = this.props

    // console.log('LayoutRouter, switch=%s', props.switch)

    // Wrap each child in a div that is hidden unless it's route is the
    // same as the current switch value

    const children = Array.isArray(props.children)? props.children  : [props.children]
    const child_routes = children.map((element, index) => {
      const show = (props.routes[index] === props.switch)? 'block' : 'none'
      const id = props.id + '-' + props.routes[index]
      return <div key={index} id={id} style={{display : show}} >{element}</div>
    });

    return (
        <div {...props} >
            {child_routes}
        </div>
    );

  }
}


LayoutRouter.propTypes = {
  /**
   * The ID of this component, used to identify dash components
   * in callbacks. The ID needs to be unique across all of the
   * components in an app.
   */
  'id': PropTypes.string,

  /**
   * The children of this component
   */
  'children': PropTypes.node,

  /**
   * A unique identifier for the component, used to improve
   * performance by React.js while rendering components
   * See https://reactjs.org/docs/lists-and-keys.html for more info
   */
  'key': PropTypes.string,

   /**
   * Often used with CSS to style elements with common properties.
   */
  'className': PropTypes.string,

  /**
   * The route to be activated
   */

  'switch' : PropTypes.string,

  /**
   * The route/switch values to be associated with each of the child routes
   */

  'routes' : PropTypes.arrayOf(PropTypes.string),

};