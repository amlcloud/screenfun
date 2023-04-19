# screenfun



**user_semsearch__create function**

Gets triggered when the machine run document is created at:
  user/{uid}/semsearch/{searchId}

gcloud functions deploy user_semsearch__create \
  --project screener-9631e \
  --entry-point user_semsearch__create \
  --runtime python37 \
  --trigger-event "providers/cloud.firestore/eventTypes/document.create" \
  --trigger-resource "projects/screener-9631e/databases/(default)/documents/user/{uid}/semsearch/{searchId}"
