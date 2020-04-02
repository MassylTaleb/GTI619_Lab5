import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getUsers } from "../../actions/users";

export class Home extends Component {
    static propTypes = {
        users: PropTypes.array.isRequired
    };

    componentDidMount() {
        this.props.getUsers();
    }

    render() {
        return (
            <div className="text-center">
                <h2>Welcome</h2>
                <p>Your email address</p>
            </div>
        )
    }
}

const mapStateToProps = state => ({
    users: state.users.users
});

export default connect(mapStateToProps, { getUsers })(Home);