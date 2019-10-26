import React, { Component } from "react";
import { NavLink } from "react-router-dom";
import "./survey.css";

class Survey extends Component {
  constructor() {
    super();
    this.state = {
      questionOne: "",
      questionTwo: "",
      questionThree: ""
    };
  }

  handleChange = e => {
    // console.log(this.state)
    this.setState({ [e.currentTarget.name]: e.currentTarget.value });
  };

  render() {
    return (
      <div className="Register-wrapper">
        <div className="Register-form">
          <form onSubmit={this.handleRegSubmit} id="main-form">
            <div className="Register-masthead">
              <img
                className="Register-logo"
                src="https://i.imgur.com/p6Cetsi.jpg"
                width={315}
                height={96}
              />
              <h5>
                <em>
                  Fill out these quick questions so we can help you find your
                  perfect dog!
                </em>
              </h5>
            </div>

            <label className="Register-label">Do you have children?</label>
            <div>
              <select className="selector">
                <option value="yes">Yes</option>
                <option value="no">No</option>
              </select>
            </div>
            <label className="Register-label">Do you have other pets?</label>
            <div>
              <select className="selector">
                <option value="cats">Cats</option>
                <option value="dogs">Dogs</option>
                <option value="other">Other</option>
              </select>
            </div>
            <label className="Register-label">
              How active would you like your dog?
            </label>
            <div>
              <select className="selector">
                <option value="high">I can run with it</option>
                <option value="moderate">I can walk with it</option>
                <option value="low">Couch potato</option>
              </select>
            </div>
            <NavLink to="/swipe">
              <button type="Submit" className="Submit-btn">
                Submit
              </button>
            </NavLink>
          </form>
        </div>
      </div>
    );
  }
}
export default Survey;
