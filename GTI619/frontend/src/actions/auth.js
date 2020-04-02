import axios from 'axios';
import {USER_LOADED, USER_LOADING, LOGIN_SUCCESS, LOGOUT_SUCCESS} from "./types";

// CHECK TOKEN & LOAD USER
export const loadUser = () => (dispatch, getState) => {
    // User loading
    dispatch({ type: USER_LOADING });

    // GET token from state
    const token = getState().auth.token;

    // Headers
    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    // If token, add to headers config
    if(token) {
        config.headers['Authorization'] = `Token ${token}`;
    }

    axios.get('/Lab5/login/', config)
        .then(res => {
            dispatch({
                type: USER_LOADED,
                payload: res.data
            })
        }).catch(err => console.log(err));
};

// LOGIN USER
export const login = (username, password) => dispatch => {

    // Headers
    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    // Request Body
    const body = JSON.stringify({ username, password });

    axios.post('/Lab5/login/', body, config)
        .then(res => {
            console.log("success");
            dispatch({
                type: LOGIN_SUCCESS,
                payload: res.data
            })
        }).catch(err => console.log(err));
};

// LOG OUT USER
export const logout = () => (dispatch, getState) => {

    // GET token from state
    const token = getState().auth.token;

    // Headers
    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    // If token, add to headers config
    if(token) {
        config.headers['Authorization'] = `Token ${token}`;
    }

    axios
        .post("/Lab5/logout/", null, config)
        .then(res => {
            dispatch({
                type: LOGOUT_SUCCESS
            })
        }).catch(err => console.log(err));
};