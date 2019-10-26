class SourceSerializer < ActiveModel::Serializer
  has_many :pets
  attributes :id, :name
end
