"""Toast API Json Schema List.
"""

RECIPIENT_SCHEMA = {
    'type': 'object',
    'properties': {
        'recipientNo':              { 'type': 'string' },
        'countryCode':              { 'type': 'string' },
        'internationalRecipientNo': { 'type': 'string' },
        'templateParameter':        { 'type': 'object' },
        'recipientGroupingKey':     { 'type': 'string' }
    },
    'required': ['recipientNo']
}


QUERY_SCHEMA = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        'sendType':             { 'type': 'string', 
                                  'enum': ['sms', 'mms'] },
        'requestId':            { 'type': 'string' },
        'startRequestDate':     { 'type': 'string',
                                  'pattern': '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}' },
        'endRequestDate':       { 'type': 'string',
                                  'pattern': '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}' },
        'startResultDate':      { 'type': 'string',
                                  'pattern': '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}' },
        'endResultDate':        { 'type': 'string',
                                  'pattern': '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}' },
        'sendNo':               { 'type': 'string' },
        'recipientNo':          { 'type': 'string' },
        'templateId':           { 'type': 'string' },
        'msgStatus':            { 'type': 'string' },        
        'resultCode':           { 'type': 'string',
                                  'enum': ['MTR1', 'MTR2'] },                
        'subResultCode':        { 'type': 'string',
                                  'enum': ['MTR_1', 'MTR_2', 'MTR_3'] },                
        'senderGroupingKey':    { 'type': 'string' },                
        'recipientGroupingKey': { 'type': 'string' },
        'pageNum':              { 'type': 'integer' },
        'pageSize':             { 'type': 'integer' }
    },
    'required': ['sendType'],
    'anyOf' : [
        { 'required' : ['requestId'] },
        { 'required' : ['startRequestDate', 'endRequestDate'] }
    ],

}


TAG_SCHEMA = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        'sendType':          { 'type': 'string', 
                               'enum': ['sms', 'mms'] },        
        'sendNo':            { 'type': 'string' },
        'templateId':        { 'type': 'string' },
        'templateParameter': { 'type': 'object' },
        'title':             { 'type': 'string' },
        'body':              { 'type': 'string' },
        'tagExpression':     { 'type': 'array',
                               'items': { 'type': 'string' } },
        'attachFileIdList':  { 'type': 'array', 
                               'items': { 'type': 'integer' } },
        'userId':            { 'type': 'string' },
        'requestDate':       { 'type': 'string', 
                               'pattern': '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}' },
        'adYn':              { 'type': 'string', 
                               'enum': ['Y', 'N'] },
        'autoSendYn':        { 'type': 'string', 
                               'enum': ['Y', 'N'] } },
    'required': ['sendNo', 'tagExpression', 'sendType'],
    'anyOf' : [
        {
            'if': { 'properties': { 'sendType': {'const': 'mms'} } },
            'then': { 'required' : ['title', 'body'] },
            'else': { 'required': ['body'] }
        },
        { 'required' : ['templateId'] }
    ],
    'additionalProperties': False
}

REQUEST_SCHEMA = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'definitions': {
        'recipient': RECIPIENT_SCHEMA
    },
    'type': 'object',
    'properties': {
        'sendType':          { 'type': 'string', 
                               'enum': ['sms', 'mms'] },
        'templateId':        { 'type': 'string' },
        'title':             { 'type': 'string' },
        'body':              { 'type': 'string' },
        'sendNo':            { 'type': 'string' },
        'requestDate':       { 'type': 'string', 
                               'pattern': '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}' },
        'senderGroupingKey': { 'type': 'string' },
        'attachFileIdList':  { 'type': 'array', 
                               'items': { 'type': 'integer' } },
        'recipientList':     { 'type': 'array',
                               'items': { '$ref': '#/definitions/recipient' },
                               'minItems': 1,
                               'maxItems': 1000 },
        'userId':            { 'type': 'string' } },
    'required': ['sendNo', 'recipientList', 'sendType'],
    'anyOf' : [
        {
            'if': { 'properties': { 'sendType': {'const': 'mms'} } },
            'then': { 'required' : ['title', 'body'] },
            'else': { 'required': ['body'] }
        },
        { 'required' : ['templateId'] }
    ],
    'additionalProperties': False
}


UPLOAD_SCHEMA = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        'fileName':   { 'type': 'string' },
        'createUser': { 'type': 'string' },
        'fileBody':   { 'type': 'array',
                        'items': { 'type': 'string' } }
    },
    'required': ['fileName', 'createUser', 'fileBody'],
    'additionalProperties': False
}


CATEGORY_SCHEMA = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        'categoryParentId':   { 'type': 'integer' },
        'categoryName':       { 'type': 'string' },
        'categoryDesc':       { 'type': 'string' },
        'useYn':              { 'type': 'string',
                                'enum': ['Y', 'N'] },
        'createUser':         { 'type': 'string' },
        'updateUser':         { 'type': 'string' },
    },
    'required': ['categoryName', 'useYn'],
    'additionalProperties': False
}


TEMPLATE_SCHEMA = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        'categoryId':       { 'type': 'integer' },
        'templateId':       { 'type': 'string' },
        'templateName':     { 'type': 'string' },
        'templateDesc':     { 'type': 'string' },
        'sendNo':           { 'type': 'string' },
        'sendType':         { 'type': 'string',
                              'enum': ['0', '1'] },
        'title':            { 'type': 'string' },
        'body':             { 'type': 'string' },
        'useYn':            { 'type': 'string',
                              'enum': ['Y', 'N'], },
        'attachFileIdList': { 'type': 'array',
                              'items': { 'type': 'integer' } }
    },
    'required': ['categoryId', 'templateId', 'templateName', 'sendNo', 'sendType', 'body', 'useYn'],
    'if': { 
        'properties': { 'sendType': {'const': '1' } } 
    },
    'then': {
        'required': ['title'],
    },
    'additionalProperties': False    
}

