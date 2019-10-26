class Pet < ActiveRecord::Base
  has_many :swipes
end