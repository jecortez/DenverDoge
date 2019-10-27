import React, { useEffect, useState } from "react";
import Swipeable from "react-swipy";
import { useClient } from "react-fetching-library";

import Card from "../components/Card";
import Button from "../components/Button";

const appStyles = {
  height: "100%",
  display: "flex",
  justifyContent: "center",
  // alignItems: "center",
  margin: "4rem",
  width: "100%",
  minHeight: "100vh",
  fontFamily: "sans-serif",
  overflow: "hidden"
};

const wrapperStyles = { position: "relative", width: "250px", height: "250px" };
const actionsStyles = {
  display: "flex",
  justifyContent: "space-between",
  marginTop: 12
};

const cardsQuery = () => ({
  endpoint: "http://denver-doge.us-east-1.elasticbeanstalk.com/api/v1/pets"
});

export default function SwipeForm() {
  const [cards, setCards] = useState([
    {
      id: "1",
      name: "Melon",
      description: "So sweet",
      breeds_primary: "lab",
      image_url:
        "https://images.unsplash.com/photo-1548199973-03cce0bbc87b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80",
      age: "4",
      gender: "female",
      attributes_activity_level: "active",
      attributes_spayed_neutered: "true",
      attributes_house_trained: "true",
      attributes_declawed: "false",
      attributes_special_needs: "false",
      attributes_shots_current: "true",
      environment_children: "true",
      environment_dogs: "true",
      environment_cats: "true"
    },
    {
      id: "2",
      name: "Mango",
      description: "So sweet",
      breeds_primary: "lab",
      image_url:
        "https://images.unsplash.com/photo-1554693190-383dd5302125?ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=60",
      age: "4",
      gender: "female",
      attributes_activity_level: "active",
      attributes_spayed_neutered: "true",
      attributes_house_trained: "true",
      attributes_declawed: "false",
      attributes_special_needs: "false",
      attributes_shots_current: "true",
      environment_children: "true",
      environment_dogs: "true",
      environment_cats: "true"
    },
    {
      id: "3",
      name: "Butterscotch",
      description: "So sweet",
      breeds_primary: "lab",
      image_url:
        "https://images.unsplash.com/photo-1547494911-2aa9e3fad3b0?ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=60",
      age: "5",
      gender: "male",
      attributes_activity_level: "active",
      attributes_spayed_neutered: "true",
      attributes_house_trained: "true",
      attributes_declawed: "false",
      attributes_special_needs: "false",
      attributes_shots_current: "true",
      environment_children: "true",
      environment_dogs: "true",
      environment_cats: "true"
    }
  ]);
  const [isLoading, setIsLoading] = useState(true);
  const { query } = useClient();
  useEffect(() => {
    fetch("http://denver-doge.us-east-1.elasticbeanstalk.com/api/v1/pets")
      .then(res => res.json())
      .then(
        (result) => {
          setCards(result);
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
        }
      );
  }, [query]);

  const remove = () => {
    setCards(cards.slice(1, cards.length));
  };

  return (
    <div style={appStyles}>
      <div style={wrapperStyles}>
        {cards.length > 0 && (
          <div style={wrapperStyles}>
            <Swipeable
              buttons={({ right, left }) => (
                <div className="btn__container" style={actionsStyles}>
                  <Button onClick={left}>Reject</Button>
                  <Button onClick={right}>Accept</Button>
                </div>
              )}
              onAfterSwipe={remove}
            >
              {cards[0] && <Card cardAttributes={cards[0]} />}
            </Swipeable>
          </div>
        )}
      </div>
    </div>
  );
}
