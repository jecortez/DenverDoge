Rails.application.routes.draw do
  root 'welcome#hello_world'

  get '/welcome', to: 'welcome#hello_world'

  namespace 'api' do
    namespace 'v1' do
      resources :pets, only: [:index, :show]
    end
  end
end
