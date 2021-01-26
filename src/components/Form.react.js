import React, { Component } from 'react';
import PropTypes from 'prop-types';

/**
 * The `Form` components normal submit action is inhibited. Instead the forms 
 * data, as it would be reported by the default form action, is collected and is
 * available via the form_data attribute.
 */
class Form extends Component {

  constructor(props) {
    super(props);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  /**
   * Iterate over form fields
   * 
   * @param elements 
   */

  getFormFields(elements) {
    const obj = {}
    for (let i = 0; i < elements.length; i++) {

      const item = elements.item(i);

      if (!item) continue;

      if (item.type === 'checkbox') {
        obj[item.id] = item.checked;
        continue;
      }

      if (item.type === 'radio') {
        if (item.checked) obj[item.name] = item.value;
        continue;
      }

      if (item.name) obj[item.name] = item.value;
    }
    
    return obj;
  }

  /**
   * Process form submit
   * 
   * @param e 
   */

  handleSubmit(e) {
    if (this.props.preventDefault) e.preventDefault();
    const form_data = this.getFormFields(e.currentTarget.elements);
    this.props.setProps({ form_data })
  }

  render() {
    const { children, loading_state, ...otherProps } = this.props;
    return (
      <form
        {...otherProps}
        onSubmit={e => this.handleSubmit(e)}
        data-dash-is-loading={
          (loading_state && loading_state.is_loading) || undefined
        }
      >
        {children}
      </form>
    );
  }
}

Form.propTypes = {
  /**
   * The ID of this component, used to identify dash components
   * in callbacks. The ID needs to be unique across all of the
   * components in an app.
   */
  id: PropTypes.string,

  /**
   * The children of this component
   */
  children: PropTypes.node,

  /**
   * Defines CSS styles which will override styles previously set.
   */
  style: PropTypes.object,

  /**
   * Often used with CSS to style elements with common properties.
   */
  className: PropTypes.string,

  /**
   * A unique identifier for the component, used to improve
   * performance by React.js while rendering components
   * See https://reactjs.org/docs/lists-and-keys.html for more info
   */
  key: PropTypes.string,

  /**
   * Use inline=True to apply the `form-inline` class, allowing you to display
   * a series of labels, form controls, and buttons on a single horizontal row.
   * Form controls within inline forms vary slightly from their default states.
   */
  inline: PropTypes.bool,

  /**
   * Use preventDefault=True to block the forms default action
   */

  preventDefault: PropTypes.bool,

  /**
   * The forms data as it would be reported by the default form action
   */

  form_data: PropTypes.object,

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
    component_name: PropTypes.string
  }),

  /**
   * Dash-assigned callback that should be called whenever any of the
   * properties change
   */
  setProps: PropTypes.func

};

export default Form;
