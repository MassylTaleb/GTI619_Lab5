import axios from 'axios';

import {ADD_USER, GET_USERS} from "./types";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;

// GET USERS
export const getUsers = () => dispatch =>{
    axios
        .get("/Lab5/")
        .then(res => {
            dispatch({
                type: GET_USERS,
                payload: res.data
            })
        }).catch(err => console.log(err));
};

// ADD USER
export const addUser = (user) => dispatch => {
    axios
        .post("/Lab5/signup/", user)
        .then(res => {
            dispatch({
                type: ADD_USER,
                payload: res.data
            });
        }).catch(err => console.log(err));
};