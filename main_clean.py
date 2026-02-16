import cleaner

raw_names = ["  maKKiiew", "ACCHan egawa", " kikkle_macc "]
user_bio = "Hi, I'm Makkiiew and my email is contact@example.com for business."

clean_names = cleaner.standardize_names(raw_names)

found_email = cleaner.extract_email(user_bio)

print(f"Cleaned Names: {clean_names}")
print(f"Found Email:  {found_email}")
