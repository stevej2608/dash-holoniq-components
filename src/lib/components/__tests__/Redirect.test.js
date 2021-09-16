

import React from 'react';
import { shallow } from 'enzyme';
import Redirect from '../Redirect.react';


const setProps = jest.fn()  
window.scrollTo = jest.fn()

delete global.window.location;
global.window = Object.create(window);
global.window.location = {
  pathname: '',
  port: '',
  protocol: '',
  hostname: '',
};

describe('<Redirect />', () => {

    test('Several redirect components work together', () => {

        const redirect1 = shallow((
            <Redirect id='redirect1' setProps={setProps}/>
        ));

        const redirect2 = shallow((
            <Redirect id='redirect2' setProps={setProps}/>
        ));

        // First redirect

        redirect1.setProps({ href: '/test/redirect1' });
        expect(location.pathname).toEqual('/test/redirect1')

        // Second redirect

        redirect2.setProps({ href: '/test/redirect2' });
        expect(location.pathname).toEqual('/test/redirect2')

        // First redirect again

        redirect1.setProps({ href: '/test/redirect1' });
        expect(location.pathname).toEqual('/test/redirect1')


    });

});
