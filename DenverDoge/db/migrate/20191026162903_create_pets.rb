class CreatePets < ActiveRecord::Migration[6.0]
  def change
    create_table :pets do |t|
      t.references :source, null: false, foreign_key: true
      t.string :batch_id
      t.string :external_id
      t.string :url
      t.string :type
      t.string :species
      t.string :age
      t.string :gender
      t.string :size
      t.string :coat
      t.string :tags
      t.string :name
      t.string :description
      t.string :image_url
      t.string :status
      t.string :breeds_primary
      t.string :breeds_secondary
      t.boolean :breeds_mixed
      t.string :colors_primary
      t.string :colors_secondary
      t.string :colors_tertiary
      t.string :attributes_activity_level
      t.boolean :attributes_spayed_neutered
      t.boolean :attributes_house_trained
      t.boolean :attributes_declawed
      t.boolean :attributes_special_needs
      t.boolean :attributes_shots_current
      t.boolean :environment_children
      t.boolean :environment_dogs
      t.boolean :environment_cats
    end
  end
end
