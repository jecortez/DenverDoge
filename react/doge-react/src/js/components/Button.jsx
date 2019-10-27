import React from "react";

const buttonStyles = {
  padding: "16px 24px",
  background: "#32becd",
  cursor: "pointer",
  border: "none",
  borderRadius: 3
};

const Button = ({ children, onClick }) => (
  <button onClick={onClick} style={{ ...buttonStyles }}>
    {children}
  </button>
);

export default Button;
