class TestTimezone(unittest.TestCase):
    def test_time(self):
        fake_json = [{'Timezone':"Python"}]

        with patch('timezone.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = fake_json

            obj = Timezone()
            response = obj.get

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), fake_json)