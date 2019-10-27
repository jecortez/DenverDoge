import React from "react";

export default function Card({ cardAttributes }) {
  return (
    <div className="card center">
      <div className="card__swipe circular">
        <img className="img__circle" src={cardAttributes.image_url} />
      </div>
      <h4>{cardAttributes.name}</h4>
      <p className="card-text">{cardAttributes.description}</p>
    </div>
  );
};
