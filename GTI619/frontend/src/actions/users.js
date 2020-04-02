import axios from 'axios';

import {ADD_USER, GET_USERS} from "./types";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;

var bodyFormData = new FormData();

// GET USERS
export const getUsers = () => dispatch =>{
    axios
        .get("/Lab5/home/")
        .then(res => {
            dispatch({
                type: GET_USERS,
                payload: res.data
            })
        }).catch(err => console.log(err));
};

// ADD USER
export const addUser = user => dispatch => {
    bodyFormData.set('username', user.username);
    bodyFormData.set('email', user.email);
    bodyFormData.set('password1', user.password1);
    bodyFormData.set('password2', user.password2);
    bodyFormData.set('role', user.role);
    axios
        .post("/Lab5/signup/", user)
        .then(res => {
            dispatch({
                type: ADD_USER,
                data: bodyFormData,
                headers: { 'Content-Type': 'multipart/form-data' }
            });
        }).catch(err => console.log(err));
};