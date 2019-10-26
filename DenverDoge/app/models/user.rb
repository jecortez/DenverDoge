class User < ActiveRecord::Base
  has_one :survey
  has_many :swipes
end