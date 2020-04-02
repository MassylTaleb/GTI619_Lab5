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
            <Fragment>
                <h2>Users</h2>
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Username</th>
                            <th>Email</th>
                            <th>Role</th>
                        </tr>
                    </thead>
                    <tbody>
                        { this.props.users.map(user => (
                            <tr key={user.id}>
                                <td>{user.id}</td>
                                <td>{user.username}</td>
                                <td>{user.email}</td>
                                <td>{user.role}</td>
                                <td><button className="btn btn-danger btn-sm">
                                    Delete</button></td>
                            </tr>
                        )) }
                    </tbody>
                </table>
            </Fragment>
        )
    }
}

const mapStateToProps = state => ({
    users: state.users.users
});

export default connect(mapStateToProps, { getUsers })(Home);