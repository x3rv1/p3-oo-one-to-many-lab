class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Owner name must be a string")
        self.name = name

    def pets(self):
        """Return all pets belonging to this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Assign this owner to a pet, validating type."""
        if not isinstance(pet, Pet):
            raise Exception("add_pet requires a Pet instance")
        pet.owner = self

    def get_sorted_pets(self):
        """Return pets sorted by their names."""
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise Exception("Pet name must be a string")
        if not isinstance(pet_type, str):
            raise Exception("pet_type must be a string")
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type '{pet_type}'. Must be one of {Pet.PET_TYPES}")

        if owner is not None and not isinstance(owner, Owner):
            raise Exception("owner must be an Owner instance or None")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)