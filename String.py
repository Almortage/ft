import pyrogram

app = pyrogram.Client(
    "session_name",
    14748755,
    "f93ace2fb70ad896a5432601d8d383ad",
    in_memory=True
)

app.start()

string_session = app.export_session_string()

app.send_message("me", f"`{string_session}`")

print("\n\nCHECK SAVED MESSAGES")
