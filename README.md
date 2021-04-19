# mercadolibre_test

## description
To conquer the world you need resources and personnel.Magneto in his search for a world governed by homo superior is planning to lunch a high level invasion to all the nations in the world, but  to do so he needs an army. This code is a tool created in order to help Magneto find and recruit new mutants into his brotherhood.

## launching the project
1. create a virtual env for your project by following the instructions on https://docs.python.org/3/library/venv.html or using pycharm
   
2. on virtual env install requirements 
    ~~~~
    > pip install -r requirements.txt
    ~~~~
   
3. go to main directory 
    ~~~~
    > cd main
    ~~~~
   
4. run the server
    ~~~~
        > python manage.py runserver
    ~~~~

## manual testing the endpoints
1. with the project running call the following curl to test mutant validation endpoint
   ~~~~
   curl --location --request POST 'localhost:8000/mutant/' \
    --header 'Content-Type: application/json' \
    --data-raw ' {
            "dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
            }'
    ~~~~

2. with the project running call the following curl to test stats endpoint
   ~~~~
    curl --location --request GET 'localhost:8000/stats'
   ~~~~
   
## run unit test
4. on main folder run 
    ~~~~
        > python manage.py test
    ~~~~
   
## things to improve
1. the swagger isnt working because some changes on the library, the swagger would had been a good tool for documenting the endpoints
2. documentation, the code is missing documentation
3. memory management, although the code works, it uses a lot of vairables and this might be a problem with matrix with high number of elements, although the code tries to reduce the impact this can be improved more