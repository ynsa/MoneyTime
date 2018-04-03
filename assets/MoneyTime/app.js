import React from 'react';
import ReactDOM from 'react-dom';
import Provider from "react-redux/es/components/Provider";
import Router from "react-router-dom/es/Router";

import { App } from './components';
import store from "./store";
import history from "./constants/history";


ReactDOM.render(
    <Provider store={store}>
        <Router history={history}>
            <App/>
        </Router>
    </Provider>,
    document.getElementById('uluruclub_app')
);