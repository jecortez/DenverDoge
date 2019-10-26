import React from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";

// Logged In
// ----------------------------------
import Swipe from "./js/pages/Swipe";
import Landing from "./components/landingPage/index";
import Survey from "./components/survey/index";

const App = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/swipe" component={Swipe} />
        <Route path="/survey" component={Survey} />
        <Route path="/" component={Landing} />
      </Switch>
    </BrowserRouter>
  );
};

export default App;
