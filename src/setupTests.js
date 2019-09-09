// jest-extended
import 'jest-extended';
import {sprintf} from 'sprintf-js';


console.log = (msg, args) => {
    const str = sprintf(msg, args);
    process.stderr.write(str + '\n');
  };


// enzyme
import {configure} from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

configure({adapter: new Adapter()});
