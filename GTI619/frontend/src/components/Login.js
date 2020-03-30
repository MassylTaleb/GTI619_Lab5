import React, { Component, Fragment } from 'react';

export class Login extends Component {

    render() {
        return (
            <div className="container text-center">
                <h2>Log in to My Site</h2>
                <div className="row justify-content-center">
                    <form>
                        <div className="form-group">
                            <label htmlFor="exampleInputEmail1">Username</label>
                            <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" />
                        </div>
                        <div className="form-group">
                            <label htmlFor="exampleInputPassword1">Password</label>
                            <input type="password" className="form-control" id="exampleInputPassword1" />
                        </div>
                        <p>New to My Site? <a href="#">Sign Up!</a></p>
                        <button type="submit" className="btn btn-primary">Log In</button>
                    </form>
                </div>
            </div>
        )
    }
}

export default Login;