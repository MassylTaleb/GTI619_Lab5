import React, {Component, Fragment} from "react";

import Header from "./layout/Header";
import { HashRouter as Router, Route, Switch, Redirect } from "react-router-dom"

import { Provider } from 'react-redux';
import store from '../store'
import Login from "./accounts/Login";
import Signup from "./accounts/Signup";
import Home from "./common/Home";
import PrivateRoute from "./common/PrivateRoute";
import { loadUser } from "../actions/auth";

class App extends Component {

    componentDidMount() {
        store.dispatch(loadUser());
    }

    render() {
        return (
            <Provider store={store}>
                <Router>
                    <Fragment>
                        <Header />
                        <div className="container">
                            <Switch>
                                <Route exact path="/" component={Home} />
                                <Route exact path="/login" component={Login} />
                                <Route exact path="/signup" component={Signup} />
                            </Switch>
                        </div>
                    </Fragment>
                </Router>
            </Provider>
        )
    }
}

export default App;
