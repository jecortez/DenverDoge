import React from "react";

export default function Card({ cardAttributes }) {
  return (
    <div>
      <div className="card">
        <img
          className="card-img-top"
          src={cardAttributes.image_url}
          alt="dog card"
        />
        <h5 className="card-title">{cardAttributes.name}</h5>
        <p className="card-text">{cardAttributes.description}</p>
      </div>
    </div>
  );
}
