from .models import User

class Tracker:

    def get_user (self, email):
        user = User.objects.filter(email=email)
        if user:
            user = user[0]
        else:
            user = User(email=email, city='unk',lat=0.0,lng=0.0)
            user.save()
        return user

    def update_user_location (self, user, city, city_data):
        if not city_data:
            user.city = city
        else:
            user.city = city_data['name']
            user.country = city_data['countryName']
            user.lat = city_data['lat']
            user.lng = city_data['lng']
        user.save()