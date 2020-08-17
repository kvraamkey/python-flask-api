git filter-branch -f --env-filter "
    GIT_AUTHOR_NAME='ramki'
    GIT_AUTHOR_EMAIL='kvraamkeydev@gmail.com'
    GIT_COMMITTER_NAME='ramki'
    GIT_COMMITTER_EMAIL='kvraamkeydev@gmail.com'
  " HEAD