import React from 'react';
import { mount, shallow } from 'enzyme';
import ButtonLink from '../ButtonLink.react';

// https://jestjs.io/docs/en/23.x/using-matchers
// https://jestjs.io/docs/en/23.x/expect
//
// https://airbnb.io/enzyme/docs/api/ShallowWrapper/simulate.html
// https://stackoverflow.com/questions/43568570/how-can-i-get-window-location-pathname-on-my-test-file-using-jest
// https://medium.com/@hello_21915/testing-the-scrolltotop-component-in-react-with-enzyme-and-jest-5342fab570b4

const setProps = jest.fn()  
window.scrollTo = jest.fn()

describe('<ButtonLink />', () => {

    const click_link = (wrapper) => {
        wrapper.find('a').simulate('click', {
            preventDefault: () => {
            }
           });        
    }

    test('On click works', () => {

        const href = '/test/dest'

        expect(window.scrollTo).not.toHaveBeenCalled();
        expect(setProps).not.toHaveBeenCalled();

        const wrapper = shallow((
            <ButtonLink href={href} setProps={setProps}/>
        ));

        click_link(wrapper)

        expect(window.scrollTo).toHaveBeenCalledWith(0, 0);
        expect(setProps).toHaveBeenCalled();

        expect(location.pathname).toEqual(href)

        wrapper.setProps({ href: '/test/dest2' });
        click_link(wrapper)

        expect(location.pathname).toEqual('/test/dest2')

    });

});