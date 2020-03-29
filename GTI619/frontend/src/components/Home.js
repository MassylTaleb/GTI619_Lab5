import React, { Component } from 'react';
import { Col, Container, Row } from "reactstrap"
import {API_URL} from "../constants/Api-const";

import axios from "axios"

export class Home extends Component {

    // state = {
    //     user: []
    // };
    //
    // componentDidMount() {
    //     this.resetState();
    // }
    //
    // getUser = () => {
    //     axios.get(API_URL).then(response =>
    //         this.setState({ users: response.data }));
    // };
    //
    // resetState = () => {
    //     this.getUser()
    // };

    render() {
        return (
            <div>
                <h2>Welcome</h2>
                <p>Your email address</p>
            </div>
        )
    }
}

export default Home