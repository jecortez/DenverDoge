require 'rails_helper'

describe "pet requests" do
  xit "returns data for a single pet" do
    pet = create(:pet)

    get "/api/v1/pets/#{pet.id}"
    response_pet = JSON.parse(response.body)

    expect(response).to be_successful
  end

  xit "returns data for all pets" do
    pet = create(:pet)

    get "/api/v1/pets"
    response_pet = JSON.parse(response.body)

    expect(response).to be_successful
  end
end
