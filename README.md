
## Table of Contents

1. [Project Description](#project-description)
2.  [Installation](#installation)
3. [Authors](#authors)

## Project Description

This is the first part of the AirBnB clone, whereby our team worked on the project's backend using Python language and cmd module to make our project interactive with the user.
Our project has a storage. We integrated file storage in our application with the help of JSON.

### Command accepted in our command interpreter
1. show
2. create
3. update
4. destroy
5. count

### Examples of how these commands will be implemented
1. creating new objects(ex. user, place or state)
2. Destroying the created objects
3. updating the objects

In short words, our application does not get far away from the CRUD principle, which is used in most backend codes.
CRUD in full is create Read Update and Destroy


## Installation

```
git clone https://github.com/Yunis-konda001/alu-AirBnB_clone.git
```

After cloning, there are various directories and files under AirBnB_clone. 

Those are :
> ./console.py : The main executable of the project , the command interpreter
> 
> models/engine/file_storage.py : It is responsible to serializes intances to a Json File and deserializes Json file to instances
> 
> models/__ init __.py:  A unique `FileStorage` instance for the application
> models/base_model.py: Class that defines all common attributes/methods for other classes.
> 
> models/user.py: User class that inherits from BaseModel
> 
>models/state.py: State class that inherits from BaseModel
>
>models/city.py: City class that inherits from BaseModel
>
>models/amenity.py: Amenity class that inherits from BaseModel
>
>models/place.py: Place class that inherits from BaseModel
>
>models/review.py: Review class that inherits from BaseModel
>



``
## Author

1. Kumi Konda 
2. Shimirwa larissa noella


