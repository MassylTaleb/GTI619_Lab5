import React, { Component } from 'react';

export class Header extends Component {
    render() {
        return (
            <nav className="navbar navbar-expand-lg navbar-light bg-white">
                <a className="navbar-brand" href="#"><h3>My Site</h3></a>
                <div className="collapse navbar-collapse" id="navbarText">
                    <ul className="navbar-nav mr-auto">
                        <li className="nav-item active">
                            <a className="nav-link" href="#" /><span className="sr-only">(current)</span>
                        </li>
                        <li className="nav-item">
                            <a className="nav-link" href="#" />
                        </li>
                        <li className="nav-item">
                            <a className="nav-link" href="#" />
                        </li>
                    </ul>
                    <span className="navbar-text">
                        <a href="#">Log In</a> / <a href="#">Sign Up</a>
                    </span>
                </div>
            </nav>
        )
    }
}

export default Header