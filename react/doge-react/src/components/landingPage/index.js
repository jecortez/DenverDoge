import React, { Component } from "react";
import { NavLink } from "react-router-dom";
import "./landing.css";

class Landing extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  render() {
    return (
      <div>
        {/* Nav bar */}
        <nav class="navbar navbar-light bg-light">
          <a class="navbar-brand" href="#">
            <img
              src="https://i.imgur.com/p6Cetsi.jpg"
              width="300"
              height="65"
              alt=""
            />
          </a>
          <a class="navbar-brand" href="https://public.tableau.com/profile/trinity.moehr#!/vizhome/Dog1_15721254044560/NumberofDogsupforAdoptioninDenverMetroArea-ByRegion">
            Analytics
          </a>
          <form class="form-inline my-2 my-lg-0">
            <input
              class="form-control mr-sm-2"
              placeholder="username"
              aria-label="username"
            />
            <input
              class="form-control mr-sm-2"
              type="password"
              placeholder="password"
              aria-label="password"
            />
            <NavLink to="/swipe">
              <button
                class="btn btn-outline-success my-2 my-sm-0"
                type="submit"
              >
                Login
              </button>
            </NavLink>
          </form>
        </nav>
        {/* input forms */}
        <div class="d-flex flex-row">
          <form class="register-form col-4">
            <div class="form-group">
              <label for="exampleInputEmail1">Email address</label>
              <input
                type="email"
                class="form-control"
                id="exampleInputEmail1"
                aria-describedby="emailHelp"
                placeholder="Enter email"
              />
              <small id="emailHelp" class="form-text text-muted">
                We'll never share your email with anyone else.
              </small>
            </div>
            <div class="form-group">
              <label for="exampleInputPassword1">Password</label>
              <input
                type="password"
                class="form-control"
                id="exampleInputPassword1"
                placeholder="Password"
              />
            </div>
            {/* <div class="form-group form-check">
              <input
                type="checkbox"
                class="form-check-input"
                id="exampleCheck1"
              />
              <label class="form-check-label" for="exampleCheck1">
                Check me out
              </label>
            </div> */}
            <NavLink to="/survey">
              <button type="submit" class="btn btn-primary">
                Submit
              </button>
            </NavLink>
          </form>
          {/* Image collage */}
          <div class="dog-collage-image col-8">
            <img
              src="https://i.imgur.com/5gnmQ8V.jpg"
              alt="doggo collage"
              class="dog-collage-image"
            />
          </div>
        </div>
      </div>
    );
  }
}
export default Landing;
