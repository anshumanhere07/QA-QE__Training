OLD_EMAILS = {
    b"106210768+JadonAman@users.noreply.github.com",
    b"“iasamanjadon@gmail.com”",
}

NEW_NAME = b"Anshuman Rajput"
NEW_EMAIL = b"anshumankushwaha771@gmail.com"


def callback(commit, metadata):
    if commit.author_email in OLD_EMAILS:
        commit.author_name = NEW_NAME
        commit.author_email = NEW_EMAIL

    if commit.committer_email in OLD_EMAILS:
        commit.committer_name = NEW_NAME
        commit.committer_email = NEW_EMAIL