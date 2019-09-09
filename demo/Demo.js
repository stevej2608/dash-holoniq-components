import React, {Component} from 'react';

import {
    ButtonLink,
  } from '../src';


class Demo extends Component {

    setProps(newProps) {
        console.log("App.setProps()");
        console.log(JSON.stringify(newProps));
      }


  render() {
    return (
        <React.Fragment>)
            <h1>Dash Holoniq Components</h1>
            <ButtonLink href='#' className="btn btn-primary" setProps={this.setProps}>Hello</ButtonLink>
        </React.Fragment>
    )
  }
}
export default Demo;
