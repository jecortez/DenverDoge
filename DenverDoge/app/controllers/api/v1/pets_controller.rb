class Api::V1::PetsController < ApplicationController
  def index
    offset = rand(Pet.count)
    render json: Pet.offset(offset).limit(10)
  end

  def show
    render json: Pet.find(params[:id])
  end
end