# Phase 3 Object Relations Code Challenge - Concerts

This is my phase 3 Week 3 code challenge at Moringa School.

In this code challenge, you will be working with a Concert domain.

# Description

For this assignment, we'll be working with a Concert domain.

We have three models: `Band`, `Concert`, and `Venue`.

For our purposes, a `Band` has many `Concerts`, a `Venue` has many `Concerts`s,
and a `Concert` belongs to a `Band` and to a `Venue`.

`Band` - `Venue` is a many to many relationship.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

# Tools used
- vs code
- Pipenv
- Pytest
- Python

# Setup/Installation requirements
- Download a zip file in the code section to your desired folder
- Extract the files
- Open the extracted folder with vs code
N/B; I'm using this version of python `3.10.12` ensure you install it or change it to your desired version in the pipfile

- To get started, in the vs code run `pipenv install` while inside of this directory. 
- Then run `pipenv shell` to jump into the shell. 
- To install pytest,run `pip install pytest.`
- To run the tests, you will simply run `pytest -x` from inside of this directory;

## Deliverables

Write the following properties and methods in the classes in the files provided.
Feel free to build out any helper methods if needed.

### Initializers and Properties

#### Band

- `Band __init__(self, name, hometown)`
  - Band is initialized with a name and hometown
- `Band property name`
  - Returns the band's name
  - Names must be of type `str`
  - Must be greater than zero characters
  - Should **be able** to change after the band is instantiated
- `Band property hometown`
  - Returns the band's hometown
  - Hometowns must be of type `str`
  - Must be greater than zero characters
  - Should **not be able** to change after the band is instantiated
  - _hint: hasattr()_

#### Venue

- `Venue __init__(self, name, city)`
  - Venue is initialized with a name and city
- `Venue property name`
  - Returns the venue's name
  - names must be of type `str`
  - Must be greater than zero characters
  - Should **be able** to change after the venue is instantiated
- `Venue property city`
  - Returns the venue's city
  - Cities must be of type `str`
  - Must be greater than zero characters
  - Should **be able** to change after the venue is instantiated

#### Concert

- `Concert __init__(self, date, band, venue)`
  - Concert is initialized with a date, a `Band` instance, and `Venue` instance
- `Concert property date`
  - Returns the concert's date
  - Dates must be of type `str`
  - Must be greater than zero characters
  - Should **be able** to change after the concert is instantiated

### Object Relationship Methods and Properties

#### Concert

- `Concert band`
  - Returns the `Band` instance for this concert
  - Must be of type `Band`
  - Should **be able** to change after the concert is instantiated
- `Concert venue`
  - Returns the `Venue` instance for this concert
  - Must be of type `Venue`
  - Should **be able** to change after the concert is instantiated

#### Venue

- `Venue concerts()`
  - Returns a list of all the concerts for the venue
  - Concerts must be of type `Concert`
  - Returns `None` if there are no concerts for that venue
- `Venue bands()`
  - Returns a **unique** list of all the bands for the venue
  - Bands must be of type `Band`
  - Returns `None` if there are no concerts for that venue

#### Band

- `Band property concerts()`
  - Returns a list of all the concerts that the band has played in
  - Concerts must be of type `Concert`
  - Returns `None` if there are no concerts for that band
- `Band property venues()`
  - Returns a **unique** list of all the venues that the band has played in
  - Venues must be of type `Venue`
  - Returns `None` if there are no concerts for that band

### Aggregate and Association Methods

#### Concert

- `Concert hometown_show()`
  - Returns `True` if the concert is in the band's hometown
  - Returns `False` if it is not
- `Concert introduction()`
  - Returns a string with the band's introduction for this concert
  - An introduction is in the form:
    `"Hello {insert city name here}!!!!! We are {insert band name here} and we're from {insert hometown here}"`

#### Band

- `Band play_in_venue(venue, date)`
  - Takes a `Venue` instance and a date as arguments
  - Creates and returns a new concert object for the band in that venue on that
    date
- `Band all_introductions()`
  - Returns a list of strings representing all the introductions for this band
  - Each introduction is in the form
    `"Hello {insert city name here}!!!!! We are {insert band name here} and we're from {insert hometown here}"`
  - Returns `None` if there are no concerts

### Bonus: Aggregate and Association Method

#### Venue

- `Venue concert_on(date)`
  - Takes a date (string) as argument
  - Finds and returns the first concert object on that date at that venue
  - Returns `None` if there is no concert on that date at that venue
  - Uncomment lines 136-146 in the venue_test file

### Bonus: For any invalid inputs raise an `Exception`.

- First, **comment out** the following lines
  - **band_test.py**
    - lines 26-27, 39-40, 60-62, 65-66, 82-83
  - **concert_test.py**
    - lines 27-28, 43-44, 65-66, and 100-101
  - **venue_test.py**
    - lines 24-25, 37-38, 60-61, and 73-74
- Then, **uncomment** the following lines in the test files
  - **band_test.py**
    - lines 30-31, 43-44, 69-70, 73-74, and 86-87
  - **concert_test.py**
    - lines 31-32, 47-48, 71-72, and 106-107
  - **venue_test.py**
    - lines 28-29, 41-42, 64-65, and 77-78

# Author

SHARON OBINDA

# Support and contact details

email:: obindasharon6@gmail.com

phone:: +254769600939

# License

*Licenced under the MIT License Copyright (c) 2024 **SHARON OBINDA
