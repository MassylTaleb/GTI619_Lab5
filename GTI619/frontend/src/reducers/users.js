import { GET_USERS, ADD_USER } from '../actions/types.js';

const initialState = {
    users: []
};

export default function(state = initialState, action) {
    switch(action.type) {
        case GET_USERS:
            return {
                ...state,
                users: action.payload
            };
        case ADD_USER:
            return {
                ...state,
                users: [...state.users, action.payload]
            };
        default:
            return state;
    }
}
