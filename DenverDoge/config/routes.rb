Rails.application.routes.draw do
  root 'welcome#hello_world'

  get '/welcome', to: 'welcome#hello_world'
end
