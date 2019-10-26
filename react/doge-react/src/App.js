import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';

// Logged In
// ----------------------------------
import Swipe from './js/pages/Swipe';

const App = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/swipe" component={Swipe} />
      </Switch>
    </BrowserRouter>
  );
};

export default App;
