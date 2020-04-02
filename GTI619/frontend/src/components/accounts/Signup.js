import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

import { addUser } from "../../actions/users";

export class Signup extends Component {

    state = {
        username: "",
        email: "",
        password1: "",
        password2: "",
        role: ""
    };

    static propTypes = {
        addUser: PropTypes.func.isRequired
    };

    onChange = e => this.setState({ [e.target.name]: e.target.value });

    onSubmit = e => {
        e.preventDefault();
        const { username, email, password1, password2, role } = this.state;
        const user = { username, email, password1, password2, role };
        this.props.addUser(user);
    };

    render() {
        const { username, email, password1, password2 } = this.state;
        return (
            <div className="text-center">
                <br />
                <h2>Sign up to My Site</h2>
                <div className="row justify-content-center">
                    <form onSubmit={this.onSubmit}>
                        <div className="form-group">
                            <label htmlFor="inputUsername">Enter Username</label>
                            <input type="text" className="form-control" name="username" onChange={this.onChange}
                                   id="inputUsername" aria-describedby="usernameHelp" value={username} />
                        </div>
                        <div className="form-group">
                            <label htmlFor="inputEmail">Enter Email</label>
                            <input type="email" className="form-control" name="email" onChange={this.onChange}
                                   id="inputEmail" aria-describedby="emailHelp" value={email} />
                        </div>
                        <div className="form-group">
                            <label htmlFor="inputPassword1">Enter Password</label>
                            <input type="password" className="form-control" name="password1" onChange={this.onChange}
                                   id="inputPassword1" value={password1} />
                        </div>
                        <div className="form-group">
                            <label htmlFor="inputPassword2">Confirm Password</label>
                            <input type="password" className="form-control" name="password2" onChange={this.onChange}
                                   id="inputPassword2" value={password2} />
                        </div>
                        <div className="dropdown">
                            <button className="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenu2"
                                    data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                Dropdown
                            </button>
                            <div className="dropdown-menu" aria-labelledby="dropdownMenu2">
                                <button className="dropdown-item" type="button">Administrateur</button>
                                <button className="dropdown-item" type="button">Proposé aux clients résidentiels</button>
                                <button className="dropdown-item" type="button">Proposé aux clients clients d'affaire</button>
                            </div>
                        </div>
                        <br />
                        <button type="submit" className="btn btn-primary">Sign Up</button>
                    </form>
                </div>
            </div>
        )
    }
}

export default connect(null, { addUser })(Signup);