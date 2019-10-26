class Api::V1::PetsController < ApplicationController
  def index
    render json: Pet.all
  end

  def show
    render json: Pet.find(params[:id])
  end
end