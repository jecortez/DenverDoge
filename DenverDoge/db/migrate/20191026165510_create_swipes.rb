class CreateSwipes < ActiveRecord::Migration[6.0]
  def change
    create_table :swipes do |t|
      t.references :user, null: false, foreign_key: true
      t.references :pet, null: false, foreign_key: true
      t.boolean :liked
    end
  end
end
