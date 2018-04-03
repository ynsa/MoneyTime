import { createStore, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import rootReducer from '../reducers';

function configureStore(initialState) {
    let createStoreWithMiddleware;
    const middleware = applyMiddleware(thunk);

    createStoreWithMiddleware = compose(
        middleware
    );

    return createStoreWithMiddleware(createStore)(rootReducer, initialState);
}

function setInitialState() {
    return {};
}

let store = configureStore(setInitialState());

export default store;
