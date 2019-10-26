class WelcomeController < ApplicationController
  def hello_world
    render json: { hello: 'world' }.to_json
  end
end