import React, {Component, Fragment} from "react";
import { render } from "react-dom"

import Header from "./layout/Header";
import Home from "./Home";

class App extends Component {
    render() {
        return (
            <Fragment>
                <Header />
                <Home />
            </Fragment>
        )
    }
}

export default App;
