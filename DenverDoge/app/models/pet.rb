class Pet < ActiveRecord::Base
  has_many :swipes
  belongs_to :source
end