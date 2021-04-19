import json

from django.contrib.auth.models import User
from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APIClient

from dna_manager.models import Stats


class MutantTestCase(TestCase):
    client = Client()

    def setUp(self):
        Stats.objects.create(mutant_samples=5, human_samples=10, ratio=0.5)

    def test_validate_valid_mutant(self):
        data = {
            "dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
        }
        response = self.client.post('/mutant/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_validate_valid_human(self):
        data = {
            "dna": ["ATGCGA", "CDGTGC", "TTATGT", "AGAAGG", "CDCCTA", "TCACTG"]
        }
        response = self.client.post('/mutant/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_validate_small_sample(self):
        data = {
            "dna": ["AAA", "TTT", "CCC"]
        }
        response = self.client.post('/mutant/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_validate_invalid_mutant(self):
        data = {
            "dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG", "TCACTG"]
        }
        response = self.client.post('/mutant/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_invalid_human(self):
        data = {
            "dna": ["ATGCGA", "CDGTGC", "TTATGT", "AGAAGG", "CDCCTA", "TCACTG", "CDCCTA"]
        }
        response = self.client.post('/mutant/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_get_stats(self):
        response = self.client.get('/stats')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()[0]
        self.assertEqual(data['mutant_samples'], 5)
        self.assertEqual(data['human_samples'], 10)
        self.assertEqual(data['ratio'], 0.5)

    def test_validate_stats_update(self):
        self.test_validate_valid_human()
        response = self.client.get('/stats')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()[0]
        self.assertEqual(data['mutant_samples'], 5)
        self.assertEqual(data['human_samples'], 11)
        self.assertEqual(data['ratio'], round((5/11), 2))