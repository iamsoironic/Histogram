earnings = {
  "google": 15,
  "facebook": 12,
  "twitter": 8,
  "other": 10
}
google = "g " + earnings["google"] * "$"
facebook = "f " + earnings["facebook"] * "#"
twitter = "t " + earnings["twitter"] * "&"
other = "o " + earnings["other"] * "@"


print(google)
print(facebook)
print(twitter)
print(other)