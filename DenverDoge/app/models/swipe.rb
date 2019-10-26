class Swipe < ActiveRecord::Base
  belongs_to :pets
  belongs_to :users
end