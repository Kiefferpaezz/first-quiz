import pets_db

################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/   
#                                                                          
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is 
# created in the file `pets_db.py`. 
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each 
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

sql_pets_owned_by_nobody = sql_pets_owned_by_nobody = """

SELECT a.name, a.species, a.age
FROM animals a
WHERE a.animal_id NOT IN (SELECT pa.pet_id FROM people_animals pa);

"""


# Part 4.B:
# Write SQL to select how the number of pets are older than their owners. 
# The output should be an integer.

sql_pets_older_than_owner = sql_pets_older_than_owner = """

SELECT SUM(CASE WHEN a.age > p.age THEN 1 ELSE 0 END) AS count
FROM animals a
JOIN people_animals pa ON a.animal_id = pa.pet_id
JOIN people p ON pa.owner_id = p.person_id;

"""


# Part 4.C: BONUS CHALLENGE! 
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)
sql_only_owned_by_bessie = sql_only_owned_by_bessie = """ 

SELECT p.name, a.name, a.species
FROM animals a JOIN people_animals pa ON a.animal_id = pa.pet_id
    JOIN people p ON pa.owner_id = p.person_id
GROUP BY a.animal_id
HAVING COUNT(*) = 1 AND p.name = 'bessie';

"""
