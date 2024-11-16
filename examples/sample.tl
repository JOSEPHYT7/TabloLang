# examples/sample.tl

LOAD_HTML "form.html"
SELECT "input"
EXTRACT "name" TO user_data
EXTRACT "value" TO user_data
SAVE_TABLE user_data TO "user_data.csv"
DISPLAY_TABLE user_data
