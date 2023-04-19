from google.cloud import firestore

client = firestore.Client()

def user_semsearch__create(data, context):
    """ Triggered when document is created at /user/{uid}/semsearch/ collection.
    Args:
        data (dict): The event payload.
        context (google.cloud.functions.Context): Metadata for the event.
    """
    trigger_resource = context.resource

    print('Function triggered by change to: %s' % trigger_resource)

    path_parts = context.resource.split('/documents/')[1].split('/')
    collection_path = path_parts[0]
    document_path = '/'.join(path_parts[1:])
    master_run_doc = client.collection(collection_path).document(document_path)
    
    # proceed with semantic search and populate results in the document
    master_run_doc.update({
        'status': 'complete',
        'search_results': 'search_results'
    })