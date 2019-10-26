import React from "react";

export default function Card({ cardAttributes }) {
  return (
    <div className="card">
      <img className="card-img-top" src={cardAttributes.image_url} />
      <h5 className="card-title">{cardAttributes.name}</h5>
      <p className="card-text">{cardAttributes.description}</p>
    </div>
  );
};
