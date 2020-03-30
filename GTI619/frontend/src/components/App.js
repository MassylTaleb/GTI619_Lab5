import React, {Component, Fragment} from "react";

import Header from "./layout/Header";
import Home from "./Home";

import { Provider } from 'react-redux';
import store from '../store'
import Login from "./Login";

class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <Fragment>
                    <Header />
                    <Login />
                </Fragment>
            </Provider>
        )
    }
}

export default App;
