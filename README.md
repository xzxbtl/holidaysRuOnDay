------------------------------------
How to use?

1) You need download or update holidays lib (vacanza) check requiments.txt
2) in instance name obj pull the desired date in format (10, 4, 2024)
where 10 - day, 4 - month 2024 - year
3) if code doesn't work try to replace :
     self.secret_key = Settings.SECRET_KEY
     self.date_str = Settings.formatted_date
  on:
    self.secret_key = "Any text"
    self.date_str = "10-04-2024" date in this format
