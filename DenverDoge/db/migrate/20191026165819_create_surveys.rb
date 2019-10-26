class CreateSurveys < ActiveRecord::Migration[6.0]
  def change
    create_table :surveys do |t|
      t.references :user, null: false, foreign_key: true
      t.boolean :children
      t.boolean :dogs
      t.boolean :cats
      t.string :activity_level
    end
  end
end
