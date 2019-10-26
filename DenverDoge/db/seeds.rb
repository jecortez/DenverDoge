Swipe.delete_all
Pet.delete_all
Source.delete_all
User.delete_all

anna = User.create(name: 'Anna')

shelter = Source.create(name: 'Shelter')

password = Pet.create(name: 'Password', source_id: shelter.id)
smeagol = Pet.create(name: 'Smeagol', source_id: shelter.id)
samwise = Pet.create(name: 'Samwise', source_id: shelter.id)

Swipe.create(liked: true, user_id: anna.id, pet_id: password.id)
Swipe.create(liked: true, user_id: anna.id, pet_id: smeagol.id)
Swipe.create(liked: false, user_id: anna.id, pet_id: samwise.id)
