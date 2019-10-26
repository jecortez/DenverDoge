# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `rails
# db:schema:load`. When creating a new database, `rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 2019_10_26_165819) do

  create_table "pets", options: "ENGINE=InnoDB DEFAULT CHARSET=utf8mb4", force: :cascade do |t|
    t.bigint "source_id", null: false
    t.string "batch_id"
    t.string "external_id"
    t.string "url"
    t.string "type"
    t.string "species"
    t.string "age"
    t.string "gender"
    t.string "size"
    t.string "coat"
    t.string "tags"
    t.string "name"
    t.string "description"
    t.string "image_url"
    t.string "status"
    t.string "breeds_primary"
    t.string "breeds_secondary"
    t.boolean "breeds_mixed"
    t.string "colors_primary"
    t.string "colors_secondary"
    t.string "colors_tertiary"
    t.string "attributes_activity_level"
    t.boolean "attributes_spayed_neutered"
    t.boolean "attributes_house_trained"
    t.boolean "attributes_declawed"
    t.boolean "attributes_special_needs"
    t.boolean "attributes_shots_current"
    t.boolean "environment_children"
    t.boolean "environment_dogs"
    t.boolean "environment_cats"
    t.index ["source_id"], name: "index_pets_on_source_id"
  end

  create_table "sources", options: "ENGINE=InnoDB DEFAULT CHARSET=utf8mb4", force: :cascade do |t|
    t.string "name"
  end

  create_table "surveys", options: "ENGINE=InnoDB DEFAULT CHARSET=utf8mb4", force: :cascade do |t|
    t.bigint "user_id", null: false
    t.boolean "children"
    t.boolean "dogs"
    t.boolean "cats"
    t.string "activity_level"
    t.index ["user_id"], name: "index_surveys_on_user_id"
  end

  create_table "swipes", options: "ENGINE=InnoDB DEFAULT CHARSET=utf8mb4", force: :cascade do |t|
    t.bigint "user_id", null: false
    t.bigint "pet_id", null: false
    t.boolean "liked"
    t.index ["pet_id"], name: "index_swipes_on_pet_id"
    t.index ["user_id"], name: "index_swipes_on_user_id"
  end

  create_table "users", options: "ENGINE=InnoDB DEFAULT CHARSET=utf8mb4", force: :cascade do |t|
    t.string "name"
  end

  add_foreign_key "pets", "sources"
  add_foreign_key "surveys", "users"
  add_foreign_key "swipes", "pets"
  add_foreign_key "swipes", "users"
end
